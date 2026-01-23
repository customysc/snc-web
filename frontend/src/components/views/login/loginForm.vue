<template>
  <el-form
      style="max-width: 600px"
      :model="loginForm"
      status-icon
      label-width="auto"
      class="demo-ruleForm"
  >
    <el-form-item label="username" prop="username">
      <el-input v-model="loginForm.username"/>
    </el-form-item>
    <el-form-item label="Password" prop="pass">
      <el-input v-model="loginForm.password" type="password" autocomplete="off" />
    </el-form-item>
    <el-form-item>
      <el-button type="primary">
        Submit
      </el-button>
    </el-form-item>
  </el-form>
</template>

<script lang="ts" setup>
import { ref, reactive } from 'vue'

const loginForm = reactive({
  username: '',
  password: ''
})

</script>

