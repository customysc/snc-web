<template>
 <el-table :data="tableData" :border="true" style="width: 100%;">
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

  <el-button-group>
    <el-button size="default">
      <el-icon><ArrowLeft/></el-icon>
    </el-button>
    <el-button size="default" :disabled="true">1</el-button>
    <el-button size="default">
      <el-icon><ArrowRight/></el-icon>
    </el-button>
  </el-button-group>
</template>


<script lang="ts" setup>

import { ElTable, ElTableColumn, ElButton, ElButtonGroup, ElIcon} from 'element-plus'
import { ArrowLeft, ArrowRight } from '@element-plus/icons-vue'

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

</script>

