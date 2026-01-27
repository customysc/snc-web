<template>
  <el-carousel 
  :interval="50000" 
  autoplay
  indicator-position="bottom"
  type="card"
  :style="{height:'300px',boxShadow: '0 2px 8px rgba(0,0,0,0.1)'}"
  >
    <el-carousel-item v-for="(item, i) in banners" :key="i">
      <img 
        :src="item.src" 
        :alt="item.title"
        :style="{width:'100%',height:'100%',objectFit:'cover'}"
        />
    </el-carousel-item>
  </el-carousel>
</template>

<script setup lang="ts">
const banners = [
  { src: '/banners/image1.png', title: '轮播图1' },
  { src: '/banners/image2.png', title: '轮播图2' },
  { src: '/banners/image3.png', title: '轮播图3' },
]
</script>