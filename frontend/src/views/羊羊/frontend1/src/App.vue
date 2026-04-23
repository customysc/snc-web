<template>
  <div class="page">
    <el-page-header content="X-ware 维修工单看板" class="mb-16" />

    <el-row :gutter="16">
      <el-col
        v-for="worker in workers"
        :key="worker"
        :xs="24"
        :sm="12"
        :md="8"
        :lg="6"
      >
        <el-card class="worker-panel" shadow="hover">
          <template #header>
            <div class="worker-header">
              <span class="worker-name">{{ worker }}</span>
              <el-button type="primary" size="small" round @click="openCreateDialog(worker)">
                添加项目
              </el-button>
            </div>
          </template>

          <!-- 工作区（可接收拖拽） -->
          <div
            class="worker-body"
            :class="{ 'drag-over': dragOverWorker === worker }"
            @dragover.prevent="onDragOver($event, worker)"
            @drop.prevent="onDrop($event, worker)"
            @dragleave="onDragLeave($event, worker)"
          >
            <div v-if="store[worker].length === 0" class="empty-tip">
              暂无项目，点击“添加项目”开始录入。
            </div>

            <!-- 项目列表 -->
            <template v-else>
              <template v-for="(item, idx) in store[worker]" :key="item.id">
                <!-- 占位线：根据鼠标位置动态显示 -->
                <div
                  v-if="dropHint.worker === worker && dropHint.index === idx"
                  class="drop-placeholder show"
                ></div>

                <el-card
                  class="ticket-card"
                  shadow="never"
                  draggable="true"
                  @dragstart="onDragStart($event, worker, idx)"
                  @dragend="onDragEnd"
                  @click="openEditDialog(worker, idx)"
                >
                  <div class="ticket-title">项目 #{{ idx + 1 }}</div>
                  <div class="ticket-line"><span>姓名:</span>{{ item.name }}</div>
                  <div class="ticket-line"><span>学院:</span>{{ item.college }}</div>
                  <div class="ticket-line"><span>学号:</span>{{ item.studentId }}</div>
                  <div class="ticket-line"><span>电脑型号:</span>{{ item.deviceModel }}</div>
                  <div class="ticket-line"><span>维修项目:</span>{{ item.repairItem }}</div>
                  <div class="ticket-line"><span>报修时间:</span>{{ item.reportTime }}</div>

                  <el-button
                    class="status-btn"
                    :type="item.done ? 'success' : 'info'"
                    plain
                    @click.stop="toggleDone(worker, idx)"
                  >
                    {{ item.done ? '已维修' : '未维修' }}
                  </el-button>
                </el-card>
              </template>

              <!-- 插入到末尾时的占位线 -->
              <div
                v-if="dropHint.worker === worker && dropHint.index === store[worker].length"
                class="drop-placeholder show"
              ></div>
            </template>
          </div>
        </el-card>
      </el-col>
    </el-row>

    <!-- 添加/编辑 弹窗 -->
    <el-dialog
      v-model="formDialogVisible"
      :title="formMode === 'create' ? `为 ${currentWorker} 添加项目` : `编辑项目（${editContext?.worker}）`"
      width="620px"
      :close-on-click-modal="true"
      class="smooth-dialog"
    >
      <template #header="{ titleId, titleClass }">
        <div class="dialog-header-custom">
          <h4 :id="titleId" :class="titleClass" style="margin: 0">
            {{ formMode === 'create' ? `为 ${currentWorker} 添加项目` : `编辑项目（${editContext?.worker}）` }}
          </h4>

          <div style="display: flex; align-items: center; gap: 8px">
            <el-button
              v-if="formMode === 'edit'"
              type="danger"
              size="small"
              @click="onDeleteCurrent"
            >
              删除
            </el-button>
          </div>
        </div>
      </template>

      <el-form :model="form" :rules="rules" ref="formRef" label-width="88px">
        <el-row :gutter="12">
          <el-col :span="12">
            <el-form-item label="姓名" prop="name">
              <el-input v-model="form.name" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="学院" prop="college">
              <el-input v-model="form.college" />
            </el-form-item>
          </el-col>

          <el-col :span="12">
            <el-form-item label="学号" prop="studentId">
              <el-input v-model="form.studentId" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="电脑型号" prop="deviceModel">
              <el-input v-model="form.deviceModel" />
            </el-form-item>
          </el-col>

          <el-col :span="24">
            <el-form-item label="维修项目" prop="repairItem">
              <el-input v-model="form.repairItem" type="textarea" :rows="3" />
            </el-form-item>
          </el-col>

          <el-col :span="24">
            <el-form-item label="报修时间" prop="reportTime">
              <el-input v-model="form.reportTime" />
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>

      <template #footer>
        <el-button @click="formDialogVisible = false">取消</el-button>
        <el-button type="primary" @click="onSubmitForm">
          {{ formMode === 'create' ? '提交项目' : '保存修改' }}
        </el-button>
      </template>
    </el-dialog>

    <!-- 移动/复制确认弹窗 -->
    <el-dialog
      v-model="moveCopyDialogVisible"
      title="操作选择"
      width="420px"
      class="smooth-dialog"
    >
      <div>已拖拽到新位置，选择“移动”或“复制”。</div>
      <template #footer>
        <el-button @click="cancelMoveCopy">取消</el-button>
        <el-button type="info" @click="doCopy">复制</el-button>
        <el-button type="primary" @click="doMove">移动</el-button>
      </template>
    </el-dialog>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'

/** 人员列表 */
const workers = ref(['张三', '李四', '王五', '赵六'])

/** 工单存储：每人一个数组 */
const store = reactive({})
workers.value.forEach(w => {
  store[w] = []
})

/** 表单状态 */
const formDialogVisible = ref(false)
const formMode = ref('create') // create | edit
const currentWorker = ref('')
const editContext = ref(null) // { worker, index }

const formRef = ref()
const form = reactive({
  name: '',
  college: '',
  studentId: '',
  deviceModel: '',
  repairItem: '',
  reportTime: ''
})

const rules = {
  name: [{ required: true, message: '请输入姓名', trigger: 'blur' }],
  college: [{ required: true, message: '请输入学院', trigger: 'blur' }],
  studentId: [{ required: true, message: '请输入学号', trigger: 'blur' }],
  deviceModel: [{ required: true, message: '请输入电脑型号', trigger: 'blur' }],
  repairItem: [{ required: true, message: '请输入维修项目', trigger: 'blur' }],
  reportTime: [{ required: true, message: '请输入报修时间', trigger: 'blur' }]
}

/** 拖拽相关 */
const dragPayload = ref(null) // { fromWorker, fromIndex }
const dragOverWorker = ref('')
const dropHint = reactive({ worker: '', index: -1 }) // 占位线提示

/** 移动/复制确认 */
const moveCopyDialogVisible = ref(false)
const pendingDrop = ref(null) // { fromWorker, fromIndex, toWorker, toIndex }

function getNowTimeString() {
  const d = new Date()
  const pad = (n) => String(n).padStart(2, '0')
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())} ${pad(d.getHours())}:${pad(d.getMinutes())}:${pad(d.getSeconds())}`
}

function resetForm() {
  form.name = ''
  form.college = ''
  form.studentId = ''
  form.deviceModel = ''
  form.repairItem = ''
  form.reportTime = ''
}

/** 添加 */
function openCreateDialog(worker) {
  formMode.value = 'create'
  currentWorker.value = worker
  editContext.value = null
  resetForm()
  form.reportTime = getNowTimeString()
  formDialogVisible.value = true
}

/** 编辑 */
function openEditDialog(worker, index) {
  const item = store[worker][index]
  if (!item) return

  formMode.value = 'edit'
  currentWorker.value = ''
  editContext.value = { worker, index }

  form.name = item.name
  form.college = item.college
  form.studentId = item.studentId
  form.deviceModel = item.deviceModel
  form.repairItem = item.repairItem
  form.reportTime = item.reportTime

  formDialogVisible.value = true
}

/** 提交（创建或编辑） */
function onSubmitForm() {
  formRef.value?.validate((valid) => {
    if (!valid) return

    if (formMode.value === 'create') {
      if (!currentWorker.value) return
      store[currentWorker.value].push({
        id: crypto.randomUUID(),
        name: form.name,
        college: form.college,
        studentId: form.studentId,
        deviceModel: form.deviceModel,
        repairItem: form.repairItem,
        reportTime: form.reportTime,
        done: false
      })
      ElMessage.success('项目已添加')
    } else {
      const ctx = editContext.value
      if (!ctx) return
      const old = store[ctx.worker][ctx.index]
      if (!old) return

      store[ctx.worker][ctx.index] = {
        ...old,
        name: form.name,
        college: form.college,
        studentId: form.studentId,
        deviceModel: form.deviceModel,
        repairItem: form.repairItem,
        reportTime: form.reportTime
      }
      ElMessage.success('项目已更新')
    }

    formDialogVisible.value = false
  })
}

/** 删除当前编辑项 */
function onDeleteCurrent() {
  const ctx = editContext.value
  if (!ctx) return

  ElMessageBox.confirm('确定删除该项目吗？', '提示', {
    type: 'warning',
    confirmButtonText: '删除',
    cancelButtonText: '取消'
  }).then(() => {
    store[ctx.worker].splice(ctx.index, 1)
    formDialogVisible.value = false
    ElMessage.success('已删除')
  }).catch(() => {})
}

/** 状态切换 */
function toggleDone(worker, index) {
  const item = store[worker][index]
  if (!item) return
  item.done = !item.done
}

/** 计算插入位置 */
function getInsertIndexByMouse(containerEl, mouseY) {
  const cards = [...containerEl.querySelectorAll('.ticket-card')].filter(
    el => !el.classList.contains('dragging-shadow')
  )

  let idx = cards.length
  for (let i = 0; i < cards.length; i++) {
    const rect = cards[i].getBoundingClientRect()
    const mid = rect.top + rect.height / 2
    if (mouseY < mid) {
      idx = i
      break
    }
  }
  return idx
}

/** 拖拽开始 */
function onDragStart(evt, fromWorker, fromIndex) {
  dragPayload.value = { fromWorker, fromIndex }
  evt.dataTransfer.effectAllowed = 'copyMove'
  evt.dataTransfer.setData('text/plain', JSON.stringify(dragPayload.value))
  evt.target.classList.add('dragging-shadow')
}

/** 拖拽结束 */
function onDragEnd(evt) {
  evt.target.classList.remove('dragging-shadow')
  dragOverWorker.value = ''
  dropHint.worker = ''
  dropHint.index = -1
}

/** 拖拽经过工作区 */
function onDragOver(evt, worker) {
  dragOverWorker.value = worker
  const idx = getInsertIndexByMouse(evt.currentTarget, evt.clientY)
  dropHint.worker = worker
  dropHint.index = idx
}

/** 离开工作区 */
function onDragLeave(evt, worker) {
  if (!evt.currentTarget.contains(evt.relatedTarget)) {
    if (dragOverWorker.value === worker) dragOverWorker.value = ''
  }
}

/** 放下 */
function onDrop(evt, toWorker) {
  const text = evt.dataTransfer.getData('text/plain')
  if (!text) return

  let payload
  try {
    payload = JSON.parse(text)
  } catch {
    return
  }

  const { fromWorker, fromIndex } = payload
  if (!store[fromWorker] || !store[fromWorker][fromIndex]) return

  let toIndex = getInsertIndexByMouse(evt.currentTarget, evt.clientY)

  // 同列移动时修正
  if (fromWorker === toWorker && fromIndex < toIndex) {
    toIndex -= 1
  }

  pendingDrop.value = { fromWorker, fromIndex, toWorker, toIndex }
  moveCopyDialogVisible.value = true

  // 清理视觉提示
  dragOverWorker.value = ''
  dropHint.worker = ''
  dropHint.index = -1
}

/** 取消移动复制 */
function cancelMoveCopy() {
  pendingDrop.value = null
  moveCopyDialogVisible.value = false
}

/** 执行移动 */
function doMove() {
  const p = pendingDrop.value
  if (!p) return

  const srcList = store[p.fromWorker]
  const item = srcList[p.fromIndex]
  if (!item) return cancelMoveCopy()

  srcList.splice(p.fromIndex, 1)
  const target = store[p.toWorker]
  const safeIndex = Math.max(0, Math.min(p.toIndex, target.length))
  target.splice(safeIndex, 0, item)

  moveCopyDialogVisible.value = false
  pendingDrop.value = null
  ElMessage.success('已移动')
}

/** 执行复制 */
function doCopy() {
  const p = pendingDrop.value
  if (!p) return

  const srcList = store[p.fromWorker]
  const item = srcList[p.fromIndex]
  if (!item) return cancelMoveCopy()

  const clone = {
    ...structuredClone(item),
    id: crypto.randomUUID()
  }

  const target = store[p.toWorker]
  const safeIndex = Math.max(0, Math.min(p.toIndex, target.length))
  target.splice(safeIndex, 0, clone)

  moveCopyDialogVisible.value = false
  pendingDrop.value = null
  ElMessage.success('已复制')
}
</script>

<style scoped>
.page {
  padding: 20px;
  background: #f5f7fb;
  min-height: 100vh;
}
.mb-16 { margin-bottom: 16px; }

.worker-panel {
  border-radius: 16px;
}
.worker-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.worker-name {
  font-weight: 700;
  font-size: 17px;
}

.worker-body {
  min-height: 300px;
  border-radius: 12px;
  transition: background-color .2s ease;
}
.worker-body.drag-over {
  background: #f0f7ff;
}

.empty-tip {
  font-size: 13px;
  color: #909399;
  border: 1px dashed #dcdfe6;
  border-radius: 10px;
  padding: 10px;
  background: #fafcff;
}

.ticket-card {
  margin-bottom: 10px;
  border-radius: 12px;
  cursor: grab;
  transition: all .2s ease;
}
.ticket-card:active {
  cursor: grabbing;
}
.ticket-title {
  font-weight: 700;
  margin-bottom: 8px;
}
.ticket-line {
  font-size: 13px;
  margin: 3px 0;
  color: #374151;
}
.ticket-line span {
  color: #909399;
  margin-right: 4px;
}
.status-btn {
  width: 100%;
  margin-top: 10px;
}

.drop-placeholder {
  height: 8px;
  border-radius: 999px;
  background: #60a5fa;
  margin-bottom: 8px;
  opacity: 0;
  transform: scaleX(.8);
  transition: all .2s ease;
}
.drop-placeholder.show {
  opacity: 1;
  transform: scaleX(1);
}

/* 让弹窗过渡更明确是0.2s */
:deep(.smooth-dialog .el-dialog),
:deep(.smooth-dialog .el-overlay-dialog) {
  transition-duration: .2s !important;
}
:deep(.el-dialog) {
  border-radius: 16px;
}
.dialog-header-custom {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
</style>