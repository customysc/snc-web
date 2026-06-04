<template>
   <div class="expenditure-page">
      <!-- 页面标题 -->
      <el-page-header @back="goBack" title="返回" >
         <template #content>
            <span class="page-title">社团财务支出管理</span>
         </template>
      </el-page-header>

      <div style="margin: 16px;">
         <el-button type="primary" @click="handleAdd">新增支出记录</el-button>
      </div>
      
      <!-- 支出列表 -->
      <el-card>
         <template #header>
            <span>支出记录列表</span>
         </template>
         <el-table :data="tableData" border stripe>
            <el-table-column prop="id" label="姓名"/>
            <el-table-column prop="category" label="支出类型"/>
            <el-table-column prop="amount" label="支出金额"/>
            <el-table-column prop="approved_by" label="审批人"/>
            <el-table-column prop="created_by" label="录入人"/>
            <el-table-column label="电子发票">
               <template #default="{row}">
                  <el-button 
                     v-if="row.invoice_files" 
                     @click="handleInvoice(row.invoice_files)"
                     type="primary"
                  >
                     查看
                  </el-button>
                  <span v-else>-</span>
               </template>
            </el-table-column>
        </el-table>
      </el-card>

      <!-- 新增记录 -->
      <el-dialog v-model="addDialogVisible" title="新增支出记录" width="50%" class="add-card">
         <el-form :model="addForm" :rules="addRules" ref="addFormRef" class="add-form">
            <el-form-item label="支出类型" prop="category">
               <el-select v-model="addForm.category" placeholder="请选择支出类型">
                  <el-option 
                     v-for="cat in categoryOptions" 
                     :key="cat" 
                     :label="cat" 
                     :value="cat"
                     />
               </el-select>
            </el-form-item>
            <el-form-item label="支出金额" prop="amount">
               <el-input-number v-model="addForm.amount" placeholder="请输入支出金额"/>
            </el-form-item>
            <el-form-item label="审批人" prop="approved_by">
               <el-input v-model="addForm.approved_by" placeholder="请输入审批人姓名"/>
            </el-form-item>
            <el-form-item label="录入人" prop="created_by">
               <el-input v-model="addForm.created_by" placeholder="请输入录入人姓名"/>
            </el-form-item>
            <el-form-item label="描述" prop="description">
               <el-input v-model="addForm.description" placeholder="请输入描述"/>
            </el-form-item>
         </el-form>
         <template #footer>
            <el-button type="primary" @click="submitAddForm">提交</el-button>
            <el-button @click="addDialogVisible = false">取消</el-button>
         </template>
      </el-dialog>

      <!-- 编辑记录 -->
      <el-dialog v-model="editDialogVisible" title="编辑支出记录" width="50%" class="add-card">
         <el-form :model="editForm" :rules="editRules" ref="editFormRef" class="add-form">
            <el-form-item label="支出类型" prop="category">
               <el-select v-model="editForm.category" placeholder="请选择支出类型">
                  <el-option 
                     v-for="cat in categoryOptions" 
                     :key="cat" 
                     :label="cat" 
                     :value="cat"
                     />
               </el-select>
            </el-form-item>
            <el-form-item label="支出金额" prop="amount">
               <el-input-number v-model="editForm.amount" placeholder="请输入支出金额"/>
            </el-form-item>
            <el-form-item label="审批人" prop="approved_by">
               <el-input v-model="editForm.approved_by" placeholder="请输入审批人姓名"/>
            </el-form-item>
            <el-form-item label="录入人" prop="created_by">
               <el-input v-model="editForm.created_by" placeholder="请输入录入人姓名"/>
            </el-form-item>
            <el-form-item label="描述" prop="description">
               <el-input v-model="editForm.description" placeholder="请输入描述"/>
            </el-form-item>
         </el-form>
         <template #footer>
            <el-button type="primary" @click="submitEditForm">提交</el-button>
            <el-button @click="editDialogVisible = false">取消</el-button>
         </template>
      </el-dialog>
   </div>
</template>

<script setup>
import { ref , reactive } from 'vue'
import { ElMessage , ElMessageBox } from 'element-plus'
import { useRouter } from 'vue-router'
import http from '@/utils/axios'

const router = useRouter()

const tableData = ref([])
const getExpenditureList = async () => {
   try {
      const res = await http.get('/fin/page')
      tableData.value = res.data.result.records || []
   } catch (error) {
      ElMessage.error('获取数据失败')
      console.error(error)
   }
}
getExpenditureList()

// 支出类型选项
const categoryOptions = ref(['活动物料费', '场地与设备费用', '外勤开支', '日常开支', '其他'])

const approvedByOptions = ref([])
const getApprovedList = async () => {
   try {
      const res = await http.get('/sys/user/list')
      approvedByOptions.value = res.data.result || []
   } catch (error) {
      console.error(error)
   }
}
getApprovedList()

//弹窗控制
const addDialogVisible = ref(false)
const editDialogVisible = ref(false)

//新增表单
const addFormRef = ref(null)
const addForm = reactive({
   category: '',
   amount: '',
   approved_by: '',
   created_by: '',
   description: '',
   invoice_files: []
})

//新增表单验证规则
const addRules = {
   category: [{ required: true, message: '请选择支出类型', trigger: 'change' }],
   amount: [{ required: true, message: '请输入支出金额', trigger: 'blur' }],
   approved_by: [{ required: true, message: '请输入审批人姓名', trigger: 'blur' }],
   created_by: [{ required: true, message: '请输入录入人姓名', trigger: 'blur' }],
   description: []
}

//编辑表单验证规则
const editRules = {
   category: [{ required: true, message: '请选择支出类型', trigger: 'change' }],
   amount: [{ required: true, message: '请输入支出金额', trigger: 'blur' }],
   approved_by: [{ required: true, message: '请输入审批人姓名', trigger: 'blur' }],
   created_by: [{ required: true, message: '请输入录入人姓名', trigger: 'blur' }],
   description: []
}

//编辑表单
const editFormRef = ref(null)
const editForm = reactive({
   id: '',
   category: '',
   amount: '',
   approved_by: '',
   created_by: '',
   description: '',
   invoice_files: []
})

//返回上一页
const goBack = () => {
   router.go(-1)
}


//打开新增弹窗
const handleAdd = () => {
   addForm.category = ''
   addForm.amount = ''
   addForm.approved_by = ''
   addForm.created_by = ''
   addForm.description = ''
   addForm.invoice_files = []
   addDialogVisible.value = true
}

//打开编辑弹窗
const handleEdit = (row) => {
   editForm.id = row.id
   editForm.category = row.category || ''
   editForm.amount = row.amount || ''
   editForm.approved_by = row.approved_by || ''
   editForm.created_by = row.created_by || ''
   editForm.description = row.description || ''     
   editForm.invoice_files = row.invoice_files || []
   editDialogVisible.value = true
}

//查看发票
const handleInvoice = (url) => {
   window.open(url, '_blank')
}

const handleInvoiceSuccess = (res) => {
   ElMessage.success('上传成功!')
   addForm.invoice_files = res.FilePath
}

//提交新增表单
const submitAddForm = async () => {
   await addFormRef.value.validate()
   try {
      await http.post('/fin/add', addForm)
      ElMessage.success('新增成功!')
      addDialogVisible.value = false
      getExpenditureList()
   } catch (error) {
      ElMessage.error('新增失败')
      console.error(error)
   }
}

//提交编辑表单
const submitEditForm = async () => {
   await editFormRef.value.validate()
   try {
      await http.post('/fin/update', {
         id: editForm.id,
         category: editForm.category,
         amount: editForm.amount,
         approved_by_name: editForm.approved_by_name,
         description: editForm.description
      })
      ElMessage.success('编辑成功!')
      editDialogVisible.value = false
      getExpenditureList()
   } catch (error) {
      ElMessage.error('编辑失败')
      console.error(error)
   }
}
</script>
