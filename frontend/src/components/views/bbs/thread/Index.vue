<template>
  <div class="tieba-container" style="display: flex; width: 100%; max-width: 1200px; margin: 0 auto; background: #f9f9f9; min-height: 100vh;">
    <!-- 左侧：楼主信息栏 -->
    <div class="left-sidebar" style="width: 200px; background: #fff; padding: 16px; border-right: 1px solid #f0f0f0;">
      <img :src="ownerAvatar" :alt="ownerNickname" style="width: 80px; height: 80px; border-radius: 8px; object-fit: cover; margin-bottom: 8px;">
      <div style="font-size: 14px; color: #ff9900; font-weight: 500;">{{ ownerNickname }}</div>
      <div :style="ownerTagStyle" v-html="ownerTagText"></div>
      <span style="margin-top: 4px; font-size: 12px; color: #f56c6c; display: block;">{{ ownerIdentity }}</span>
    </div>

    <!-- 右侧：主帖+评论区 -->
    <div class="right-content" style="flex: 1; padding: 20px; background: #fff;">
      <!-- 引入主帖组件，传递动态数据 -->
      <PostMain
        :post-content="postContent"
        :post-img="postImg"
        :post-img-alt="postImgAlt"
        :post-ip="postIp"
        :post-floor="postFloor"
        :post-create-time="postCreateTime"
        :report-text="reportText"
        :reply-text="replyText"
      />

      <!-- 引入单个评论组件，循环渲染 -->
      <CommentItem
        v-for="(item, index) in commentList"
        :key="item.id"
        :item="item"
        :floor="index + 2"
        :report-text="reportText"
        :reply-text="replyText"
      />

      <!-- ElementPlus分页组件 -->
      <div style="margin: 15px 0; text-align: center;">
        <el-pagination
          v-model:current-page="currentPage"
          :page-size="pageSize"
          :total="total"
          layout="prev, pager, next"
          @current-change="handlePageChange"
          style="font-size: 12px;"
        />
      </div>

      <!-- 底部回复输入框 -->
      <div style="margin-top: 15px; padding: 10px; background: #f5f7fa; border-radius: 8px;">
        <textarea
          :placeholder="textareaPlaceholder"
          style="width: 100%; padding: 8px; border: 1px solid #e6e6e6; border-radius: 4px; resize: none; min-height: 60px;"
        ></textarea>
        <div style="text-align: right; margin-top: 8px;">
          <el-button type="primary" size="small">{{ submitBtnText }}</el-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import PostMain from './postmain.vue'
import CommentItem from './commentItem.vue'
import { ElPagination, ElButton } from 'element-plus'

// 楼主信息
const ownerAvatar = ref('https://picsum.photos/seed/louzhu/80/80') // 楼主头像
const ownerNickname = ref('硬件玩家') // 楼主昵称
const ownerTagText = ref('<span style="color: #ffd700;">⭐</span> 图吧垃圾佬') // 楼主标签
const ownerTagStyle = ref({
  marginTop: '6px',
  fontSize: '12px',
  background: '#f5f7fa',
  color: '#909399',
  padding: '2px 8px',
  borderRadius: '4px',
  display: 'inline-block'
})
const ownerIdentity = ref('楼主') // 楼主身份

// 主帖信息
const postContent = ref('刚收了一张矿渣580，大家看看这波赚了吗？') // 主帖内容
const postImg = ref('https://picsum.photos/seed/miner580/600/400') // 主帖图片
const postImgAlt = ref('矿渣580显卡') // 主帖图片alt
const postIp = ref('广东') // 主帖IP
const postFloor = ref('1楼') // 主帖楼层
const postCreateTime = ref('2026-01-23 09:00') // 主帖发布时间

// 通用文字
const reportText = ref('举报') // 举报文字
const replyText = ref('回复') // 回复文字

// 回复框信息
const textareaPlaceholder = ref('我也说一句...') // 输入框占位符
const submitBtnText = ref('发表') // 发表按钮文字

const commentList = ref([
  { id: 2, content: "赚", ipLocation: "福建", createTime: "2026-01-23 09:47", user: { avatar: "https://picsum.photos/seed/stitch/48/48", nickname: "烤红薯说是" } },
  { id: 3, content: "请问怎么看矿卡有没有修过？", ipLocation: "浙江", createTime: "2026-01-23 10:12", user: { avatar: "https://picsum.photos/seed/bear/48/48", nickname: "蕾忍宗杂役大师兄" } },
  { id: 4, content: "看焊点和电容就行", targetNickname: "蕾忍宗杂役大师兄", ipLocation: "江苏", createTime: "2026-01-23 10:25", user: { avatar: "https://picsum.photos/seed/soldier/48/48", nickname: "有猫DOS生死薄" } },
  { id: 5, content: "😏 你去搜一下矿渣580是哪个型号好吧，amd的rx580和intel的b580没一毛钱关系，b580才发布满一年", ipLocation: "河北", createTime: "2026-01-23 10:09", user: { avatar: "https://picsum.photos/seed/fish/48/48", nickname: "往事随琴" } },
  { id: 6, content: "赚，这不是rx580这是b580", ipLocation: "陕西", createTime: "2026-01-23 14:49", user: { avatar: "https://picsum.photos/seed/pikachu/48/48", nickname: "嘿嘿丶嘿小虫" } }
])

const currentPage = ref(1) // 当前页码
const pageSize = ref(5)    // 每页显示条数
const total = ref(15)      // 总评论数
// 页码切换事件
const handlePageChange = (page: number) => {
  console.log('切换到第', page, '页')
}
</script>

<style scoped>
.tieba-container {
  font-family: "Microsoft Yahei", sans-serif;
}

.left-sidebar {
  box-sizing: border-box;
}

.right-content {
  box-sizing: border-box;
}
</style>