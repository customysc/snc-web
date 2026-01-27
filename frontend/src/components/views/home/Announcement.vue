<template>
  <el-card shadow="never" :style="{ marginBottom: '10px' }">
    <template #header>
      <div :style="{ fontSize: '16px', fontWeight: 600 }">最新公告（生活相关）</div>
    </template>

    <el-empty v-if="announcements.length === 0" description="暂无公告" />
    
    <el-timeline v-else>
      <el-timeline-item
        v-for="item in announcements"
        :key="item.id"
        :timestamp="item.date"
        placement="top"
        :style="{ marginBottom: '15px' }"
      >
        <div :style="{ fontSize: '14px', fontWeight: 500 }">{{ item.title }}</div>
        <div :style="{ fontSize: '12px', color: '#666', marginTop: '4px' }">{{ item.content }}</div>
      </el-timeline-item>
    </el-timeline>
  </el-card>
</template>

<script setup lang="ts">
import { ref } from "vue";

type Announcement = {
  id: string;
  title: string;
  content: string;
  date: string;
};

const announcements = ref<Announcement[]>([
  { id: "a1", title: "系统上线", content: "欢迎使用本系统。", date: "2026-01-22" },
  { id: "a2", title: "维护通知", content: "本周末凌晨 02:00 维护。", date: "2026-01-20" },
]);
</script>