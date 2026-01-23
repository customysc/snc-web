<template>
  <el-menu
      class="el-menu-demo"
      :mode="props.menuMode"
      :default-active="$route.path"
      router
  >
    <el-menu-item index="/">首页</el-menu-item>
    <el-menu-item index="/bbs">论坛</el-menu-item>
    <el-menu-item index="/bbs/1">临时-论坛详情页跳转</el-menu-item>
    <el-menu-item index="/okr">OKR系统</el-menu-item>
    <el-menu-item index="/login">临时-登录模拟跳转</el-menu-item>
    <el-sub-menu index="2-4">
      <template #title>临时-后台排版跳转</template>
      <el-menu-item index="/admin/user">用户管理</el-menu-item>
      <el-menu-item index="/admin/role">角色管理</el-menu-item>
    </el-sub-menu>
  </el-menu>
</template>

<script setup lang="ts">
interface Props {
  menuMode?: 'horizontal' | 'vertical'
}

const props = withDefaults(defineProps<Props>(), {
  menuMode: 'horizontal'
})
</script>

