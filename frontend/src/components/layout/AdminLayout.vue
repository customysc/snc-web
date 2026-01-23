<template>
  <el-container>
    <el-container>
      <el-aside>
        <Navbar menuMode="vertical"/>
      </el-aside>
      <el-main>
        <router-view />
      </el-main>
    </el-container>
  </el-container>
</template>

<script setup lang="ts">
import Navbar from "@/components/common/Navbar.vue";
</script>
