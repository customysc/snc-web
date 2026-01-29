<template>
  <div class="flat-item" style="display: flex; padding: 10px 0; border-bottom: 1px solid #f0f0f0;">
    <!-- 左侧用户头像 -->
    <img :src="item.user.avatar" :alt="item.user.nickname" style="width: 48px; height: 48px; border-radius: 8px; object-fit: cover; flex-shrink: 0; margin-right: 8px;">
    <!-- 右侧内容区 -->
    <div style="flex: 1;">
      <div style="font-size: 15px; line-height: 1.4; color: #303133; margin-bottom: 8px;">
        <span style="color: #1989fa; font-weight: 500;">{{ item.user.nickname }}</span>
        <span v-if="item.targetNickname" style="color: #f56c6c; margin: 0 4px;">:回复 {{ item.targetNickname }}</span>
        : {{ item.content }}
      </div>
      <div style="font-size: 12px; color: #909399; display: flex; align-items: center; gap: 8px; justify-content: flex-end;">
        <span>IP属地: {{ item.ipLocation }}</span>
        <a href="#" style="color: #1989fa; text-decoration: none;">{{ reportText }}</a>
        <span>{{ floor }}楼</span>
        <span>{{ item.createTime }}</span>
        <a href="#" style="color: #1989fa; text-decoration: none;">{{ replyText }}</a>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
// 定义props，接收单条评论数据和当前楼层数、通用文字
interface Comment {
  id: number;
  content: string;
  ipLocation: string;
  createTime: string;
  targetNickname?: string;
  user: {
    avatar: string;
    nickname: string;
  };
}

defineProps<{
  item: Comment;   // 单条评论数据
  floor: number;   // 当前评论楼层数
  reportText: string; // 举报文字
  replyText: string;  // 回复文字
}>()
</script>

<style scoped>

.flat-item {
  box-sizing: border-box;
}
</style>