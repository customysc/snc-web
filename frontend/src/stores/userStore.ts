import { defineStore } from 'pinia'
import { ref } from 'vue'

interface User {
  id: number
  name: string
  avatar: string
  email: string
}

export const useUserStore = defineStore('user', () => {
  const currentUser = ref<User | null>(null)

  // 模拟登录 - 实际项目中应该从登录接口获取
  const login = (user: User) => {
    currentUser.value = user
  }

  // 模拟登出
  const logout = () => {
    currentUser.value = null
  }

  // 获取当前用户信息
  const getCurrentUser = () => {
    return currentUser.value
  }

  // 初始化默认用户（用于演示）
  const initDefaultUser = () => {
    if (!currentUser.value) {
      // 模拟张老师登录
      currentUser.value = {
        id: 1,
        name: '张老师',
        avatar: 'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png',
        email: 'teacher@example.com'
      }
    }
  }

  return {
    currentUser,
    login,
    logout,
    getCurrentUser,
    initDefaultUser
  }
})
