<template>
 <div class="contianer" style="margin-bottom: 16px;">
  <el-button 
          plain 
          size="default" 
          style="margin-right: 16px;"
        >
          导出
        </el-button>
      <el-button 
          plain 
          size="default" 
          style="margin-right: 16px;"
        >
          同步流程
        </el-button>
      <el-button 
          plain
          size="default" 
        >
          回收站
        </el-button>
  </div>

 <el-table :data="paginatedTableData" :border="true" style="width: 100%;">
   <el-table-column prop="name" label="姓名" width="240" />
   <el-table-column prop="phonenumber" label="电话号码" width="240" />
   <el-table-column prop="email" label="邮箱" width="240" :show-overflow-tooltip="true"/>
   <el-table-column prop="id" label="学工号" width="240"/>
   <el-table-column label="操作" width="360">
    <template #default>
      <el-button 
          plain 
          size="small" 
          style="margin-right: 8px;"
        >
          详情
        </el-button>
      <el-button 
          plain 
          size="small" 
          style="margin-right: 8px;"
        >
          编辑
        </el-button>
      <el-button 
          plain
          size="small" 
        >
          删除
        </el-button>
    </template>
   </el-table-column>
 </el-table>

  <div style="position:fixed;bottom:20px;right: 20px; text-align: right;">
    <el-pagination
     v-model:current-page="currentPage"
     v-model:page-size="pageSize"
     :page-sizes="[2,3,4,5]"
     layout="total,sizes,prev,pager,next"
     :total="tableData.length"
     @size-change="handleSizeChange"
     @current-change="handleCurrentChange"
    />
  </div>
</template>


<script lang="ts" setup>

import { ElTable, ElTableColumn, ElButton, ElPagination} from 'element-plus'
import { ref ,computed} from 'vue'
 
interface User {
  name: string
  phonenumber:string
  email: string
  id:string
}

const tableData : User[]=[
  {
    name: 'Aleyna Kutzner',
    phonenumber: '18020240001',
    email: '2024010001@test.com',
    id: '2024010001'
  },
  {
    name: 'Helen Jacobi',
    phonenumber: '18020240002',
    email: '2024010002@test.com',
    id: '2024010002'
  },
  {
    name: 'Brandon Deckert',
    phonenumber: '18020250001',
    email: '2025010001@test.com',
    id: '2025010001'
  },
  {
    name: 'Magie Smith',
    phonenumber: '18020250002',
    email: '2025020001@test.com',
    id: '2025020001'
  },
]

const currentPage = ref(1)
const pageSize = ref(2)

const paginatedTableData = computed(() => {
  const startIndex = (currentPage.value - 1) * pageSize.value
  const endIndex = startIndex + pageSize.value
  return tableData.slice(startIndex, endIndex)
})

const handleSizeChange = (val:number) => {
  pageSize.value = val
  currentPage.value = 1
}


const handleCurrentChange = (val: number) => {
  currentPage.value = val
}

</script>

