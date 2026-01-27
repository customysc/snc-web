<template>
  <LoginLayout>
    <template #form>
      <h2 style="text-align: center; margin-bottom: 30px; color: #333;">用户登录</h2>
      <!-- 登录表单 -->
      <el-form :model="loginForm" :rules="loginRules" ref="loginFormRef" label-position="top" hide-required-asterisk>
        <!-- 邮箱输入框 -->
        <el-form-item label="邮箱" prop="email">
          <el-input v-model="loginForm.email"  placeholder="请输入邮箱"/> </el-form-item>
        <!-- 密码输入框 -->
        <el-form-item label="密码" prop="password">
          <el-input
            v-model="loginForm.password"
            type="password"
            placeholder="请输入密码"
            show-password
          />
        </el-form-item>
        <!-- 验证码输入框 -->
        <el-form-item label="验证码" prop="captcha">
          <el-row :gutter="10">
            <el-col :span="16">
              <el-input
                v-model="loginForm.captcha"
                placeholder="验证码（演示功能）"
              />
            </el-col>
            <el-col :span="8">
              <div style="width: 100%; height: 40px; overflow: hidden; border-radius: 4px; background-color: #f5f7fa; display: flex; align-items: center; justify-content: center;">
                <div style="font-size: 12px; color: #999; text-align: center; line-height: 1.4;">验证码UI<br>待后端接入</div>
              </div>
            </el-col>
          </el-row>
        </el-form-item>
        <!-- 登录按钮 -->
        <el-form-item>
          <el-button type="primary" @click="handleLogin" style="width: 100%;">登录</el-button>
        </el-form-item>
        <!-- 底部链接 -->
        <div style="display: flex; justify-content: space-between; margin-top: 20px;">
          <el-link type="primary" :href="router.resolve({ name: 'ForgotPassword' }).href">忘记密码？</el-link>
          <el-link type="primary" :href="router.resolve({ name: 'Register' }).href">注册账号</el-link>
        </div>
      </el-form>
    </template>
  </LoginLayout>
</template>

<script lang="ts" setup>
// 导入依赖
import { ref, reactive } from 'vue'
import { ElMessage, type FormInstance, type FormRules } from 'element-plus'
import router from "@/routes";
import LoginLayout from "@/components/views/login/LoginLayout.vue";

// 表单实例
const loginFormRef = ref<FormInstance>()

// 表单数据
const loginForm = reactive({
  email: '',
  password: '',
  captcha: '' // 验证码字段，暂为演示
})

// 验证规则
const loginRules: FormRules = {
  email: [
    { required: true, message: '请输入邮箱地址', trigger: 'blur' },
    { type: 'email', message: '请输入正确的邮箱格式', trigger: 'blur' }
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' }
  ]
  // 验证码验证规则暂不启用
}

// 登录处理
const handleLogin = () => {
  loginFormRef.value?.validate((valid: boolean) => {
    if (valid) {
      ElMessage.success('登录成功')
      // 实际项目中这里应该调用登录接口
    } else {
      ElMessage.warning('账号或密码错误，请重新输入')
      return false
    }
  })
}

</script>
