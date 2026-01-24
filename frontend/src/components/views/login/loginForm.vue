<template>
  <!-- 登录页面容器 -->
  <div class="login-container">
    <!-- 登录卡片 -->
    <el-card class="login-card">
      <h2 class="login-title">用户登录</h2>
      <!-- 登录表单 -->
      <el-form :model="loginForm" :rules="loginRules" ref="loginFormRef" label-position="top" hide-required-asterisk>
        <!-- 邮箱输入框 -->
        <el-form-item label="邮箱" prop="email">
          <el-input 
            v-model="loginForm.email" 
            placeholder="请输入邮箱"
          />
        </el-form-item>
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
              <div class="captcha-image">
                <div class="captcha-text">验证码UI<br>待后端接入</div>
              </div>
            </el-col>
          </el-row>
        </el-form-item>
        <!-- 登录按钮 -->
       <el-form-item>            <el-button type="primary" @click="handleLogin" style="width: 100%;">登录</el-button>
        </el-form-item>
        <!-- 底部链接 -->
        <div class="login-footer">
          <el-link type="primary" @click="showForgotPassword = true">忘记密码？</el-link>
          <el-link type="primary" @click="showRegister = true">注册账号</el-link>
        </div>
      </el-form>
    </el-card>

    <!-- 注册弹窗 -->
    <el-dialog v-model="showRegister" title="用户注册" width="400px">
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
          <el-button @click="showRegister = false">取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>

    <!-- 忘记密码弹窗 -->
    <el-dialog v-model="showForgotPassword" title="忘记密码" width="400px">
      <el-form :model="forgotPasswordForm" :rules="forgotPasswordRules" ref="forgotPasswordFormRef">
        <!-- 忘记密码表单 -->
        <el-form-item label="邮箱" prop="email">
          <el-input v-model="forgotPasswordForm.email" placeholder="请输入注册时的邮箱" />
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="handleForgotPassword">发送重置链接</el-button>
          <el-button @click="showForgotPassword = false">取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>

<script lang="ts" setup>
// 导入依赖
import { ref, reactive } from 'vue'
import { ElMessage, type FormInstance, type FormRules } from 'element-plus'

// 表单实例
const loginFormRef = ref<FormInstance>()
const registerFormRef = ref<FormInstance>()
const forgotPasswordFormRef = ref<FormInstance>()

// 表单数据
const loginForm = reactive({
  email: '',
  password: '',
  captcha: '' // 验证码字段，暂为演示
})

const registerForm = reactive({
  email: '',
  password: '',
  confirmPassword: ''
})

const forgotPasswordForm = reactive({
  email: ''
})

// 弹窗控制
const showRegister = ref(false)
const showForgotPassword = ref(false)

// 密码确认验证
const validateConfirmPassword = (_rule: any, value: string, callback: any) => {
  if (value !== registerForm.password) {
    callback(new Error('两次输入的密码不一致'))
  } else {
    callback()
  }
}

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

const forgotPasswordRules: FormRules = {
  email: [
    { required: true, message: '请输入邮箱地址', trigger: 'blur' },
    { type: 'email', message: '请输入正确的邮箱格式', trigger: 'blur' }
  ]
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

// 注册处理
const handleRegister = () => {
  registerFormRef.value?.validate((valid: boolean) => {
    if (valid) {
      ElMessage.success('注册表单验证通过（演示）')
      showRegister.value = false
      // 实际项目中这里应该调用注册接口
    } else {
      ElMessage.warning('请检查表单')
      return false
    }
  })
}

// 忘记密码处理
const handleForgotPassword = () => {
  forgotPasswordFormRef.value?.validate((valid: boolean) => {
    if (valid) {
      ElMessage.success('密码重置链接已发送（演示）')
      showForgotPassword.value = false
      // 实际项目中这里应该调用发送重置链接接口
    } else {
      ElMessage.warning('请检查表单')
      return false
    }
  })
}
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f5f5f5;
}

.login-card {
  width: 400px;
  padding: 30px;
}

.login-title {
  text-align: center;
  margin-bottom: 30px;
  color: #333;
}

/* 验证码样式 */
.captcha-image {
  width: 100%;
  height: 40px;
  overflow: hidden;
  border-radius: 4px;
  background-color: #f5f7fa;
  display: flex;
  align-items: center;
  justify-content: center;
}

.captcha-text {
  font-size: 12px;
  color: #999;
  text-align: center;
  line-height: 1.4;
}

/* 底部链接样式 */
.login-footer {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}
</style>
```