<template>
  <div class="flat-item owner-post" style="padding: 10px 0; border-bottom: 1px solid #f0f0f0;">
    <!-- 主帖文字内容 -->
    <div style="font-size: 15px; line-height: 1.4; color: #303133; margin-bottom: 8px;">
      {{ postContent }}
    </div>
    <!-- 楼主发布的图片 -->
    <div class="owner-image" style="margin-bottom: 8px;">
      <img :src="postImg" :alt="postImgAlt" style="max-width: 100%; border-radius: 8px; object-fit: cover;">
    </div>
    <div style="font-size: 12px; color: #909399; display: flex; align-items: center; gap: 8px; justify-content: flex-end;">
      <span>IP属地: {{ postIp }}</span>
      <a href="#" style="color: #1989fa; text-decoration: none;">{{ reportText }}</a>
      <span>{{ postFloor }}</span>
      <span>{{ postCreateTime }}</span>
      <a href="#" style="color: #1989fa; text-decoration: none;">{{ replyText }}</a>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  postContent: string;    // 主帖内容
  postImg: string;        // 主帖图片地址
  postImgAlt: string;     // 主帖图片alt
  postIp: string;         // 主帖IP属地
  postFloor: string;      // 主帖楼层
  postCreateTime: string; // 主帖发布时间
  reportText: string;     // 举报文字
  replyText: string;      // 回复文字
}>()
</script>

<style scoped>

.owner-image img {
  max-width: 600px; 
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}
.owner-post {
  margin: 0;
}
</style>