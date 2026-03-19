<template>
   <!-- 操作按钮区域 -->
 <div class="contianer" style="margin-bottom: 16px;">
  <el-button plain size="default" style="margin-right: 16px;">导出</el-button>
      <el-button plain size="default" style="margin-right: 16px;">同步流程</el-button>
      <el-button plain size="default">回收站</el-button>
  </div>
 <!--用户信息表格-->
 <el-table :data="tableData" :border="true" style="width: 100%;">
   <el-table-column prop="username" label="姓名" width="240" />
   <el-table-column prop="student_no" label="学工号" width="240" />
   <el-table-column prop="email" label="邮箱" width="240" :show-overflow-tooltip="true"/>
   <el-table-column prop="id" label="ID" width="240"/>
   <el-table-column label="操作" width="360">
    <!--操作列-->
    <template #default>
      <el-button plain size="small" style="margin-right: 8px;">详情</el-button>
      <el-button plain size="small" style="margin-right: 8px;">编辑</el-button>
      <el-button plain size="small">删除</el-button>
    </template>
   </el-table-column>
 </el-table>
 <!--分页组件-->
  <div>
    <el-pagination
     v-model:current-page="currentPage"
     v-model:page-size="pageSize"
     :page-sizes="[20]"
     layout="total,sizes,prev,pager,next"
     :total="total"
     @size-change="handleSizeChange"
     @current-change="handleCurrentChange"
    />
  </div>
</template>


<script lang="ts" setup>

import { ElTable, ElTableColumn, ElButton, ElPagination} from 'element-plus'
import {ref, onMounted} from 'vue'
import type {SysUser} from "@/views/admin/user/user.data.ts";
import {userPageApi} from "@/views/admin/user/user.api.ts";

const tableData = ref<SysUser[]>([]);

const currentPage = ref(1);
const pageSize = ref(20);
const total = ref(0);

const handleSizeChange = (val:number) => {
  pageSize.value = val;
}

const handleGetList = async (params?) => {

  const res = await userPageApi(params);
  const data = res.data;
  const result = data.result;
  tableData.value = result.records;
  total.value = result.total;
}

const handleCurrentChange = (val: number) => {
  currentPage.value = val
  handleGetList({'page_size': pageSize.value, 'current_page': currentPage.value});
}

onMounted(() => {
  handleGetList();
})

</script>

