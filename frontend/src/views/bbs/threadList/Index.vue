<template>
  <!-- 极简页面容器：仅保留宽度、居中、基础内边距 -->
  <div style="width: 100%; max-width: 1200px; margin: 0 auto; padding: 10px;">
    <h1>论坛帖子列表</h1>

    <div>
      <!-- 帖子列表：仅保留基础循环和布局 -->
      <div v-for="item in threadList" :key="item.id" style="margin-bottom: 15px;">
        <!-- 帖子标题：仅保留点击事件和基础展示 -->
        <div @click="handleClickThread(item.id)">
          {{ item.title }}
        </div>

        <!-- 帖子摘要：仅保留文本展示 -->
        <div>{{ item.summary }}</div>

        <!-- 多图展示：仅保留基础尺寸和布局 -->
        <div style="display: flex;">
          <img 
            v-for="(url, index) in item.imgUrls.slice(0, 3)" 
            :key="index"
            :src="url" 
            :alt="`${item.title} 图片${index+1}`"
            style="width: 80px; height: 80px;"
          >
          <!-- 超过3张的提示：仅保留基础展示 -->
          <div v-if="item.imgUrls.length > 3">
            +{{ item.imgUrls.length - 3 }}
          </div>
        </div>

        <!-- 帖子元信息：仅保留flex布局和文本展示 -->
        <div style="display: flex; justify-content: space-between;">
          <span>作者：{{ item.author }}</span>
          <span>发布时间：{{ item.createTime }}</span>
          <span>阅读量：{{ item.readCount }}</span>
        </div>
      </div>

      <!-- 分页：仅保留基础功能展示 -->
      <div style="display: flex; justify-content: center;">
        <el-pagination
          v-model:current-page="currentPage"
          v-model:page-size="pageSize"
          :total="total"
          layout="prev, pager, next, jumper, ->, total"
          @current-change="handlePageChange"
        />
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import { ref, reactive, toRefs } from 'vue'

// 帖子数据类型接口（支持多图）
interface ThreadItem {
  id: number
  title: string
  summary: string
  author: string
  createTime: string
  readCount: number
  imgUrls: string[]  // 改为数组，存多张图片地址
}

interface Pagination {
  currentPage: number
  pageSize: number
  total: number
}

// 模拟数据（包含多图帖子）
const threadList = ref<ThreadItem[]>([
  {
    id: 1,
    title: 'Vue3 + Vite 项目搭建避坑指南',
    summary: '本文详细讲解了Vue3 + Vite + TS项目的搭建步骤，以及新手常见的报错和解决方案。',
    author: '前端小白',
    createTime: '2026-01-20',
    readCount: 1258,
    imgUrls: ['https://picsum.photos/seed/vue3/80/80']  // 单图
  },
  {
    id: 2,
    title: 'Element Plus 行内样式使用技巧',
    summary: '行内样式在Vue3中的使用规范，驼峰命名的注意事项，以及如何通过行内样式快速调试页面布局。',
    author: '样式控',
    createTime: '2026-01-19',
    readCount: 896,
    imgUrls: ['https://picsum.photos/seed/element/80/80', 'https://picsum.photos/seed/css/80/80']  // 双图
  },
  {
    id: 3,
    title: '内存不够，硬盘来凑',
    summary: '去年220买的内存今年1000卖掉了。朋友他的两个16g 4000频率说涨到150...',
    author: '瑞丹枫',
    createTime: '2026-01-18',
    readCount: 1560,
    imgUrls: [
      'https://picsum.photos/seed/ram/80/80', 
      'https://picsum.photos/seed/hdd/80/80', 
      'https://picsum.photos/seed/ssd/80/80', 
      'https://picsum.photos/seed/pc/80/80'
    ]  // 四图（显示前3张+“+1”）
  }
])

const pagination = reactive<Pagination>({
  currentPage: 1,
  pageSize: 3,
  total: 9
})
const { currentPage, pageSize, total } = toRefs(pagination)

const handleClickThread = (threadId: number) => {
  alert(`你点击了帖子 ID：${threadId}，可在此处跳转至帖子详情页`)
}

const handlePageChange = (page: number) => {
  console.log(`切换到第 ${page} 页`)
}
</script>