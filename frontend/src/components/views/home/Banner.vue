<template>
  <el-carousel :interval="10000" type="card" height="200px">
    <el-carousel-item v-for="src in banners" :key="src">
      <img class="w-full h-full" :src="src" alt="banner"/>
    </el-carousel-item>
  </el-carousel>
</template>

<script setup lang="ts">
const banners = [
  'banners/image1.png',
  'banners/image2.png',
  'banners/image3.png',
]
</script>
