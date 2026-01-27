<template>
  <LoginFormLayout>
    <template #form>
      <el-form :model="forgotPasswordForm" :rules="forgotPasswordRules" ref="forgotPasswordFormRef">
        <!-- 忘记密码表单 -->
        <el-form-item label="邮箱" prop="email">
          <el-input v-model="forgotPasswordForm.email" placeholder="请输入注册时的邮箱" />
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="handleForgotPassword">发送重置链接</el-button>
          <el-button>取消</el-button>
        </el-form-item>
      </el-form>
    </template>
  </LoginFormLayout>
</template>

<script setup lang="ts">

import LoginFormLayout from "@/components/views/login/LoginLayout.vue";
import {reactive, ref} from "vue";
import {ElMessage, type FormInstance, type FormRules} from "element-plus";
const forgotPasswordForm = reactive({
  email: ''
})
const forgotPasswordFormRef = ref<FormInstance>()

const forgotPasswordRules: FormRules = {
  email: [
    { required: true, message: '请输入邮箱地址', trigger: 'blur' },
    { type: 'email', message: '请输入正确的邮箱格式', trigger: 'blur' }
  ]
}

// 忘记密码处理
const handleForgotPassword = () => {
  forgotPasswordFormRef.value?.validate((valid: boolean) => {
    if (valid) {
      ElMessage.success('密码重置链接已发送（演示）')
      // 实际项目中这里应该调用发送重置链接接口
    } else {
      ElMessage.warning('请检查表单')
      return false
    }
  })
}
</script>
