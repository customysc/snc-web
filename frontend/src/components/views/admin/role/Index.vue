<template>
  <el-button info @click="table = true">
    授权
  </el-button>

  <el-drawer
      v-model="table"
      title="授权"
      direction="rtl"
      size="50%"
  >

   角色权限配置:
   <el-tree
    v-model="value"
    :data="data"
    multiple
    :render-after-expand="false"
    show-checkbox
    style="width: 300px"
    default-expand-all="true"
   />
   
   <div style="position:fixed;bottom: 20px;right: 20px;">
      <el-button>取消</el-button>
      <el-button>仅保存</el-button>
      <el-button>保存并关闭</el-button>
    </div>
  </el-drawer>
</template>

<script lang="ts" setup>
import { ref } from 'vue'

const table = ref(false)

const value = ref()

const data = [
  {
    value: '1',
    label: 'Level one 1',
    children: [
      {
        value: '1-1',
        label: 'Level two 1-1',
        children: [
          {
            value: '1-1-1',
            label: 'Level three 1-1-1',
          },
        ],
      },
    ],
  },
  {
    value: '2',
    label: 'Level one 2',
    children: [
      {
        value: '2-1',
        label: 'Level two 2-1',
        children: [
          {
            value: '2-1-1',
            label: 'Level three 2-1-1',
          },
        ],
      },
      {
        value: '2-2',
        label: 'Level two 2-2',
        children: [
          {
            value: '2-2-1',
            label: 'Level three 2-2-1',
          },
        ],
      },
    ],
  },
  {
    value: '3',
    label: 'Level one 3',
    children: [
      {
        value: '3-1',
        label: 'Level two 3-1',
        children: [
          {
            value: '3-1-1',
            label: 'Level three 3-1-1',
          },
        ],
      },
      {
        value: '3-2',
        label: 'Level two 3-2',
        children: [
          {
            value: '3-2-1',
            label: 'Level three 3-2-1',
          },
        ],
      },
    ],
  },
]

</script>
