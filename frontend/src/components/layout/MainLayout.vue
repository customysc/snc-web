<template>
  <el-container>
    <el-header>
      <Navbar/>
    </el-header>
    <el-main>
      <div class="tw:w-[60vw] tw:mx-auto">
        <router-view/>
      </div>
    </el-main>
  </el-container>
</template>

<script setup lang="ts">
import Navbar from "@/components/common/Navbar.vue";
</script>
