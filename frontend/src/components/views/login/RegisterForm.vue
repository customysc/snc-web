<template>
  <LoginFormLayout>
    <template #form>
      <el-form :model="registerForm" :rules="registerRules" ref="registerFormRef">
        <!-- 注册表单 -->
        <el-form-item label="邮箱" prop="email">
          <el-input v-model="registerForm.email" placeholder="请输入邮箱" />
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input
              v-model="registerForm.password"
              type="password"
              placeholder="请输入密码"
              show-password
          />
        </el-form-item>
        <el-form-item label="确认密码" prop="confirmPassword">
          <el-input
              v-model="registerForm.confirmPassword"
              type="password"
              placeholder="请再次输入密码"
              show-password
          />
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="handleRegister">注册</el-button>
          <el-button>取消</el-button>
        </el-form-item>
      </el-form>
    </template>
  </LoginFormLayout>
</template>

<script setup lang="ts">

import LoginFormLayout from "@/components/views/login/LoginLayout.vue";
import {ElMessage, type FormInstance, type FormRules} from "element-plus";
import {reactive, ref} from "vue";

const registerFormRef = ref<FormInstance>()

const registerForm = reactive({
  email: '',
  password: '',
  confirmPassword: ''
})

// 密码确认验证
const validateConfirmPassword = (_rule: any, value: string, callback: any) => {
  if (value !== registerForm.password) {
    callback(new Error('两次输入的密码不一致'))
  } else {
    callback()
  }
}
const registerRules: FormRules = {
  email: [
    { required: true, message: '请输入邮箱地址', trigger: 'blur' },
    { type: 'email', message: '请输入正确的邮箱格式', trigger: 'blur' }
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' },
    { min: 6, message: '密码长度不能少于6位', trigger: 'blur' }
  ],
  confirmPassword: [
    { required: true, message: '请再次输入密码', trigger: 'blur' },
    { validator: validateConfirmPassword, trigger: 'blur' }
  ]
}

// 注册处理
const handleRegister = () => {
  registerFormRef.value?.validate((valid: boolean) => {
    if (valid) {
      ElMessage.success('注册表单验证通过（演示）')
      // 实际项目中这里应该调用注册接口
    } else {
      ElMessage.warning('请检查表单')
      return false
    }
  })
}
</script>
