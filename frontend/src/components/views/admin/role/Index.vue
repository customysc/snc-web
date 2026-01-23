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
    在这里加个树表
  </el-drawer>
</template>

<script lang="ts" setup>
import { ref } from 'vue'

const table = ref(false)

</script>
