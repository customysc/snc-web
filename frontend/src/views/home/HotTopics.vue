<template>
  <el-card shadow="never">
    <template #header>
      热点
    </template>
    <el-empty v-if="hotTopics.length === 0" description="暂无热点" />
    <div v-else>
      <div
          v-for="h in hotTopics"
          :key="h.id"
          class="tw:flex tw:justify-between"
      >
        <div>
          <div>{{ h.title }}</div>
          <div>{{ h.desc }}</div>
        </div>
        <el-tag size="small" type="danger" effect="plain">{{ h.heat }}</el-tag>
      </div>
    </div>
  </el-card>
</template>
<script setup lang="ts">
import {ref} from "vue";
type HotTopic = {
  id: string;
  title: string;
  desc: string;
  heat: string;
};
const hotTopics = ref<HotTopic[]>([
  { id: "h1", title: "OKR 看板更新", desc: "支持进度与评分分离展示。", heat: "HOT" },
  { id: "h2", title: "权限体系讨论", desc: "RBAC + 用户特例策略。", heat: "↑" },
]);
</script>