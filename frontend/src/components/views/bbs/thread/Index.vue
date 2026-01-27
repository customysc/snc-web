<template>
  <div class="tieba-container" style="display: flex; width: 100%; max-width: 1200px; margin: 0 auto; background: #f9f9f9; min-height: 100vh;">
    <!-- 左侧：楼主信息栏（保留） -->
    <div class="left-sidebar" style="width: 200px; background: #fff; padding: 16px; border-right: 1px solid #f0f0f0;">
      <img 
        src="https://picsum.photos/seed/louzhu/80/80" 
        alt="硬件玩家"
        style="width: 80px; height: 80px; border-radius: 8px; object-fit: cover; margin-bottom: 8px;"
      >
      <div style="font-size: 14px; color: #ff9900; font-weight: 500;">硬件玩家</div>
      <div style="margin-top: 6px; font-size: 12px; background: #f5f7fa; color: #909399; padding: 2px 8px; border-radius: 4px; display: inline-block;">
        <span style="color: #ffd700;">⭐</span> 图吧垃圾佬
      </div>
      <span style="margin-top: 4px; font-size: 12px; color: #f56c6c; display: block;">楼主</span>
    </div>

    <!-- 右侧：主帖+全平级评论区 -->
    <div class="right-content" style="flex: 1; padding: 20px; background: #fff;">
      <!-- 主帖（1楼）：贴左显示，紧凑样式 -->
      <div class="flat-item owner-post" style="padding: 10px 0; border-bottom: 1px solid #f0f0f0;">
        <!-- 主帖文字内容 -->
        <div style="font-size: 15px; line-height: 1.4; color: #303133; margin-bottom: 8px;">
          刚收了一张矿渣580，大家看看这波赚了吗？
        </div>
        <!-- 楼主发布的图片 -->
        <div class="owner-image" style="margin-bottom: 8px;">
          <img 
            src="https://picsum.photos/seed/miner580/600/400" 
            alt="矿渣580显卡"
            style="max-width: 100%; border-radius: 8px; object-fit: cover;"
          >
        </div>
        <div style="font-size: 12px; color: #909399; display: flex; align-items: center; gap: 8px; justify-content: flex-end;">
          <span>IP属地: 广东</span>
          <a href="#" style="color: #1989fa; text-decoration: none;">举报</a>
          <span>1楼</span>
          <span>2026-01-23 09:00</span>
          <a href="#" style="color: #1989fa; text-decoration: none;">回复</a>
        </div>
      </div>

      <!-- 其他评论（2-6楼）：紧凑样式 -->
      <div 
        v-for="(item, index) in commentList" 
        :key="item.id"
        class="flat-item"
        style="display: flex; padding: 10px 0; border-bottom: 1px solid #f0f0f0;"
      >
        <!-- 左侧用户头像（缩小尺寸） -->
        <img 
          :src="item.user.avatar" 
          :alt="item.user.nickname"
          style="width: 48px; height: 48px; border-radius: 8px; object-fit: cover; flex-shrink: 0; margin-right: 8px;"
        >

        <!-- 右侧内容区（紧凑行高） -->
        <div style="flex: 1;">
          <div style="font-size: 15px; line-height: 1.4; color: #303133; margin-bottom: 8px;">
            <span style="color: #1989fa; font-weight: 500;">{{ item.user.nickname }}</span>
            <span v-if="item.targetNickname" style="color: #f56c6c; margin: 0 4px;">:回复 {{ item.targetNickname }}</span>
            : {{ item.content }}
          </div>

          <div style="font-size: 12px; color: #909399; display: flex; align-items: center; gap: 8px; justify-content: flex-end;">
            <span>IP属地: {{ item.ipLocation }}</span>
            <a href="#" style="color: #1989fa; text-decoration: none;">举报</a>
            <span>{{ index + 2 }}楼</span>
            <span>{{ item.createTime }}</span>
            <a href="#" style="color: #1989fa; text-decoration: none;">回复</a>
          </div>
        </div>
      </div>

      <!-- 分页样式（仅展示，无实际功能） -->
      <div style="margin: 15px 0; text-align: center;">
        <button 
          style="
            padding: 4px 12px;
            margin: 0 4px;
            border: 1px solid #f56c6c;
            background-color: #f5f5f5;
            color: #f56c6c;
            border-radius: 4px;
            cursor: default;
            font-size: 12px;
          "
        >
          1
        </button>
        <button 
          style="
            padding: 4px 12px;
            margin: 0 4px;
            border: 1px solid #e6e6e6;
            background-color: #fff;
            color: #303133;
            border-radius: 4px;
            cursor: pointer;
            font-size: 12px;
          "
        >
          2
        </button>
        <button 
          style="
            padding: 4px 12px;
            margin: 0 4px;
            border: 1px solid #e6e6e6;
            background-color: #fff;
            color: #303133;
            border-radius: 4px;
            cursor: pointer;
            font-size: 12px;
          "
        >
          3
        </button>
      </div>

      <!-- 底部回复输入框 -->
      <div style="margin-top: 15px; padding: 10px; background: #f5f7fa; border-radius: 8px;">
        <textarea 
          placeholder="我也说一句..." 
          style="width: 100%; padding: 8px; border: 1px solid #e6e6e6; border-radius: 4px; resize: none; min-height: 60px;"
        ></textarea>
        <div style="text-align: right; margin-top: 8px;">
          <button style="padding: 4px 12px; background: #1989fa; color: #fff; border: none; border-radius: 4px; cursor: pointer;">发表</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

// 评论数据
const commentList = ref([
  {
    id: 2,
    content: "赚",
    ipLocation: "福建",
    createTime: "2026-01-23 09:47",
    user: {
      avatar: "https://picsum.photos/seed/stitch/48/48",
      nickname: "烤红薯说是"
    }
  },
  {
    id: 3,
    content: "请问怎么看矿卡有没有修过？",
    ipLocation: "浙江",
    createTime: "2026-01-23 10:12",
    user: {
      avatar: "https://picsum.photos/seed/bear/48/48",
      nickname: "蕾忍宗杂役大师兄"
    }
  },
  {
    id: 4,
    content: "看焊点和电容就行",
    targetNickname: "蕾忍宗杂役大师兄",
    ipLocation: "江苏",
    createTime: "2026-01-23 10:25",
    user: {
      avatar: "https://picsum.photos/seed/soldier/48/48",
      nickname: "有猫DOS生死薄"
    }
  },
  {
    id: 5,
    content: "😏 你去搜一下矿渣580是哪个型号好吧，amd的rx580和intel的b580没一毛钱关系，b580才发布满一年",
    ipLocation: "河北",
    createTime: "2026-01-23 10:09",
    user: {
      avatar: "https://picsum.photos/seed/fish/48/48",
      nickname: "往事随琴"
    }
  },
  {
    id: 6,
    content: "赚，这不是rx580这是b580",
    ipLocation: "陕西",
    createTime: "2026-01-23 14:49",
    user: {
      avatar: "https://picsum.photos/seed/pikachu/48/48",
      nickname: "嘿嘿丶嘿小虫"
    }
  }
])
</script>

<style scoped>
.tieba-container {
  font-family: "Microsoft Yahei", sans-serif;
}
/* 移除主帖的右移间距，让内容贴左 */
.owner-post {
  margin: 0;
}
/* 楼主图片样式优化 */
.owner-image img {
  max-width: 600px; /* 限制图片最大宽度，避免溢出 */
  box-shadow: 0 1px 3px rgba(0,0,0,0.1); /* 轻微阴影提升质感 */
}
</style>