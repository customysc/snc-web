<template>
  <div class="xware-page">
    <el-page-header content="X-ware 维修工单看板" style="margin-bottom: 16px" />

    <!-- 工具栏 -->
    <div class="toolbar">
      <div class="toolbar-left">
        <el-radio-group v-model="viewMode" size="default">
          <el-radio-button value="kanban">看板视图</el-radio-button>
          <el-radio-button value="table">表格视图</el-radio-button>
        </el-radio-group>
        <el-select v-model="filterStatus" placeholder="筛选状态" clearable style="width: 140px; margin-left: 12px">
          <el-option v-for="s in statusOptions" :key="s" :label="s" :value="s" />
        </el-select>
        <el-input v-model="searchText" placeholder="搜索姓名/学号/问题" clearable style="width: 200px; margin-left: 12px" />
      </div>
      <div class="toolbar-right">
        <el-select v-model="sortField" placeholder="排序字段" style="width: 130px">
          <el-option label="报修时间" value="appointment_time" />
          <el-option label="姓名" value="name" />
          <el-option label="状态" value="status" />
        </el-select>
        <el-button @click="toggleSortOrder" style="margin-left: 4px">
          {{ sortOrder === 'asc' ? '↑' : '↓' }}
        </el-button>
        <el-button type="primary" @click="openCreateDialog" style="margin-left: 12px">新增工单</el-button>
      </div>
    </div>

    <!-- 看板视图 -->
    <div v-if="viewMode === 'kanban'" class="kanban-container">
      <div v-for="status in statusOptions" :key="status" class="kanban-column">
        <div class="column-header">
          <span class="column-title">{{ status }}</span>
          <el-tag size="small" type="info">{{ getColumnItems(status).length }}</el-tag>
        </div>
        <div
          class="column-body"
          :class="{ 'drag-over': dragOverStatus === status }"
          @dragover.prevent="onDragOver($event, status)"
          @drop.prevent="onDrop($event, status)"
          @dragleave="onDragLeave($event, status)"
        >
          <div v-if="getColumnItems(status).length === 0" class="empty-tip">暂无工单</div>
          <template v-for="(item, idx) in getColumnItems(status)" :key="item.id">
            <div
              v-if="dropHint.status === status && dropHint.index === idx"
              class="drop-placeholder show"
            ></div>
            <el-card
              class="ticket-card"
              shadow="hover"
              draggable="true"
              @dragstart="onDragStart($event, item)"
              @dragend="onDragEnd"
              @click="openEditDialog(item)"
            >
              <div class="ticket-title">{{ item.name || '未填写' }}</div>
              <div class="ticket-line"><span>学院:</span>{{ item.department }}</div>
              <div class="ticket-line"><span>学号:</span>{{ item.student_no }}</div>
              <div class="ticket-line"><span>电脑:</span>{{ item.computer }}</div>
              <div class="ticket-line"><span>问题:</span>{{ item.issue }}</div>
              <div class="ticket-line"><span>预约:</span>{{ item.appointment_time }}</div>
            </el-card>
          </template>
          <div
            v-if="dropHint.status === status && dropHint.index === getColumnItems(status).length"
            class="drop-placeholder show"
          ></div>
        </div>
      </div>
    </div>

    <!-- 表格视图 -->
    <div v-if="viewMode === 'table'" class="table-container">
      <el-table :data="filteredAndSorted" border stripe style="width: 100%" @sort-change="onTableSort">
        <el-table-column prop="name" label="姓名" width="100" sortable="custom" />
        <el-table-column prop="student_no" label="学号" width="120" sortable="custom" />
        <el-table-column prop="department" label="学院" width="120" sortable="custom" />
        <el-table-column prop="computer" label="电脑型号" width="130" />
        <el-table-column prop="issue" label="问题描述" min-width="180" show-overflow-tooltip />
        <el-table-column prop="appointment_time" label="预约时间" width="170" sortable="custom" />
        <el-table-column prop="status" label="状态" width="110" sortable="custom">
          <template #default="{ row }">
            <el-tag :type="statusTagType(row.status)">{{ row.status || '未设置' }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column prop="result" label="结果" width="100" />
        <el-table-column label="操作" width="140" fixed="right">
          <template #default="{ row }">
            <el-button size="small" @click="openEditDialog(row)">编辑</el-button>
            <el-button size="small" type="danger" @click="onDelete(row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>

    <!-- 新增/编辑弹窗 -->
    <el-dialog v-model="dialogVisible" :title="dialogTitle" width="640px" :close-on-click-modal="true">
      <el-form :model="form" :rules="rules" ref="formRef" label-width="90px">
        <el-row :gutter="12">
          <el-col :span="12">
            <el-form-item label="姓名" prop="name">
              <el-autocomplete v-model="form.name" :fetch-suggestions="(q:string, cb:any) => fetchSuggestion('name', q, cb)" placeholder="姓名" style="width:100%" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="学院" prop="department">
              <el-autocomplete v-model="form.department" :fetch-suggestions="(q:string, cb:any) => fetchSuggestion('department', q, cb)" placeholder="学院" style="width:100%" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="学号" prop="student_no">
              <el-autocomplete v-model="form.student_no" :fetch-suggestions="(q:string, cb:any) => fetchSuggestion('student_no', q, cb)" placeholder="学号" style="width:100%" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="电脑型号" prop="computer">
              <el-autocomplete v-model="form.computer" :fetch-suggestions="(q:string, cb:any) => fetchSuggestion('computer', q, cb)" placeholder="电脑型号" style="width:100%" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="联系电话" prop="phone">
              <el-input v-model="form.phone" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="状态" prop="status">
              <el-select v-model="form.status" style="width:100%">
                <el-option v-for="s in statusOptions" :key="s" :label="s" :value="s" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item label="问题描述" prop="issue">
              <el-input v-model="form.issue" type="textarea" :rows="2" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="预约时间">
              <el-date-picker v-model="form.appointment_time" type="datetime" placeholder="选择时间" style="width:100%" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="结果">
              <el-select v-model="form.result" clearable style="width:100%">
                <el-option label="已解决" value="已解决" />
                <el-option label="未解决" value="未解决" />
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
      <template #footer>
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" @click="onSubmit">{{ isEdit ? '保存' : '提交' }}</el-button>
      </template>
    </el-dialog>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, computed, onMounted } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import type { XWOrderItem } from './xware.api'
import { getOrderPage, addOrder, updateOrder, deleteOrder, getSuggestions } from './xware.api'

const statusOptions = ['New', 'Ready', 'Running', 'Blocked', 'Terminated']
const viewMode = ref<'kanban' | 'table'>('kanban')
const filterStatus = ref('')
const searchText = ref('')
const sortField = ref('appointment_time')
const sortOrder = ref<'asc' | 'desc'>('desc')

const orders = ref<XWOrderItem[]>([])
const dialogVisible = ref(false)
const isEdit = ref(false)
const formRef = ref()
const form = reactive<XWOrderItem>({
  name: '', student_no: '', department: '', phone: '', computer: '',
  issue: '', appointment_time: '', status: 'New', result: '',
})

const suggestionsCache = reactive<Record<string, string[]>>({})

const rules = {
  name: [{ required: true, message: '请输入姓名', trigger: 'blur' }],
  issue: [{ required: true, message: '请输入问题描述', trigger: 'blur' }],
}

const dialogTitle = computed(() => isEdit.value ? '编辑工单' : '新增工单')

const filteredAndSorted = computed(() => {
  let list = [...orders.value]
  if (filterStatus.value) {
    list = list.filter(i => i.status === filterStatus.value)
  }
  if (searchText.value) {
    const q = searchText.value.toLowerCase()
    list = list.filter(i =>
      (i.name || '').toLowerCase().includes(q) ||
      (i.student_no || '').toLowerCase().includes(q) ||
      (i.issue || '').toLowerCase().includes(q)
    )
  }
  list.sort((a: any, b: any) => {
    const va = a[sortField.value] || ''
    const vb = b[sortField.value] || ''
    const cmp = va < vb ? -1 : va > vb ? 1 : 0
    return sortOrder.value === 'asc' ? cmp : -cmp
  })
  return list
})

function getColumnItems(status: string) {
  return filteredAndSorted.value.filter(i => i.status === status)
}

function statusTagType(status: string) {
  const map: Record<string, string> = { New: 'info', Ready: 'warning', Running: '', Blocked: 'danger', Terminated: 'success' }
  return map[status] || 'info'
}

function toggleSortOrder() {
  sortOrder.value = sortOrder.value === 'asc' ? 'desc' : 'asc'
}

function onTableSort({ prop, order }: any) {
  if (prop) sortField.value = prop
  sortOrder.value = order === 'ascending' ? 'asc' : 'desc'
}

// Drag and drop
const dragPayload = ref<XWOrderItem | null>(null)
const dragOverStatus = ref('')
const dropHint = reactive({ status: '', index: -1 })

function onDragStart(evt: DragEvent, item: XWOrderItem) {
  dragPayload.value = item
  evt.dataTransfer!.effectAllowed = 'move'
  ;(evt.target as HTMLElement).style.opacity = '0.5'
}

function onDragEnd(evt: DragEvent) {
  ;(evt.target as HTMLElement).style.opacity = '1'
  dragOverStatus.value = ''
  dropHint.status = ''
  dropHint.index = -1
}

function onDragOver(evt: DragEvent, status: string) {
  dragOverStatus.value = status
  const container = evt.currentTarget as HTMLElement
  const cards = [...container.querySelectorAll('.ticket-card')]
  let idx = cards.length
  for (let i = 0; i < cards.length; i++) {
    const rect = cards[i].getBoundingClientRect()
    if (evt.clientY < rect.top + rect.height / 2) { idx = i; break }
  }
  dropHint.status = status
  dropHint.index = idx
}

function onDragLeave(evt: DragEvent, status: string) {
  if (!(evt.currentTarget as HTMLElement).contains(evt.relatedTarget as Node)) {
    if (dragOverStatus.value === status) dragOverStatus.value = ''
  }
}

async function onDrop(_evt: DragEvent, toStatus: string) {
  const item = dragPayload.value
  if (!item || item.status === toStatus) {
    dragOverStatus.value = ''
    dropHint.status = ''
    dropHint.index = -1
    return
  }
  item.status = toStatus
  try {
    await updateOrder({ id: item.id, status: toStatus })
    ElMessage.success(`已移动到 ${toStatus}`)
  } catch { ElMessage.error('移动失败') }
  dragOverStatus.value = ''
  dropHint.status = ''
  dropHint.index = -1
}

// CRUD
async function loadOrders() {
  try {
    const res = await getOrderPage(1, 200)
    orders.value = res.data?.result?.records || []
  } catch { orders.value = [] }
}

function resetForm() {
  Object.assign(form, { id: undefined, name: '', student_no: '', department: '', phone: '', computer: '', issue: '', appointment_time: '', status: 'New', result: '' })
}

function openCreateDialog() {
  isEdit.value = false
  resetForm()
  dialogVisible.value = true
}

function openEditDialog(item: XWOrderItem) {
  isEdit.value = true
  Object.assign(form, { ...item })
  dialogVisible.value = true
}

async function onSubmit() {
  await formRef.value?.validate()
  try {
    if (isEdit.value) {
      await updateOrder({ ...form })
      ElMessage.success('已更新')
    } else {
      await addOrder({ ...form })
      ElMessage.success('已创建')
    }
    dialogVisible.value = false
    await loadOrders()
  } catch { ElMessage.error('操作失败') }
}

async function onDelete(item: XWOrderItem) {
  await ElMessageBox.confirm('确定删除该工单？', '提示', { type: 'warning' })
  try {
    await deleteOrder(item.id!)
    ElMessage.success('已删除')
    await loadOrders()
  } catch { ElMessage.error('删除失败') }
}

// Autocomplete suggestions
async function fetchSuggestion(field: string, query: string, cb: any) {
  if (!suggestionsCache[field]) {
    try {
      const res = await getSuggestions(field)
      suggestionsCache[field] = res.data?.result || []
    } catch { suggestionsCache[field] = [] }
  }
  const list = suggestionsCache[field]
  const filtered = query ? list.filter(v => v.toLowerCase().includes(query.toLowerCase())) : list
  cb(filtered.map(v => ({ value: v })))
}

onMounted(loadOrders)
</script>

<style scoped>
.xware-page { padding: 20px; background: #f5f7fb; min-height: 100vh; }
.toolbar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; flex-wrap: wrap; gap: 8px; }
.toolbar-left, .toolbar-right { display: flex; align-items: center; }
.kanban-container { display: flex; gap: 12px; overflow-x: auto; padding-bottom: 12px; }
.kanban-column { min-width: 260px; flex: 1; background: #fff; border-radius: 12px; padding: 12px; }
.column-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px; }
.column-title { font-weight: 700; font-size: 15px; }
.column-body { min-height: 200px; border-radius: 8px; transition: background .2s; }
.column-body.drag-over { background: #ecf5ff; }
.empty-tip { font-size: 13px; color: #909399; text-align: center; padding: 20px 0; }
.ticket-card { margin-bottom: 8px; border-radius: 10px; cursor: grab; }
.ticket-card:active { cursor: grabbing; }
.ticket-title { font-weight: 700; margin-bottom: 6px; }
.ticket-line { font-size: 13px; margin: 2px 0; color: #374151; }
.ticket-line span { color: #909399; margin-right: 4px; }
.drop-placeholder { height: 6px; border-radius: 999px; background: #409eff; margin-bottom: 6px; opacity: 0; transition: all .2s; }
.drop-placeholder.show { opacity: 1; }
.table-container { background: #fff; border-radius: 12px; padding: 16px; }
</style>
