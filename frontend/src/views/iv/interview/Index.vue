<template>
  <div>
    <el-button>新增</el-button>
    <el-button>导出</el-button>
    <el-button>导入</el-button>
    <el-dropdown v-if="selectedRowKeys.length > 0">
      <template #dropdown>
        <el-dropdown-menu>
          <el-dropdown-item>删除</el-dropdown-item>
        </el-dropdown-menu>
      </template>
      <el-button>
        批量操作
      </el-button>
    </el-dropdown>
  </div>
  <el-table :data="tableData" border style="width: 100%">
    <el-table-column type="selection" :selectable="selectedRowKeys" width="55"/>
    <el-table-column
        v-for="col in columns"
        :key="col.prop"
        v-bind="col"
    />
  </el-table>
</template>

<script lang="ts" setup>
import {columns} from './data'
import {ElButton} from "element-plus";
import {ref} from "vue";
const selectedRowKeys = (row: any) => true;
const tableData = [
  {
    date: '2016-05-03',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
  {
    date: '2016-05-02',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
  {
    date: '2016-05-04',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
  {
    date: '2016-05-01',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
]
</script>
