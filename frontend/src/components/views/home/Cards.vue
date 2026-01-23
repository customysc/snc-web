<template>
  <div class="tw:grid tw:grid-cols-3 tw:gap-4">
  <el-card
        v-for="site in sites"
        :key="site.key"
        shadow="hover"
        class="tw:cursor-pointer"
    >
      <div class="tw:flex tw:items-start tw:gap-4">
        <!-- 左侧图标 -->
        <el-icon :size="40">
          <component :is="site.icon" />
        </el-icon>

        <!-- 右侧文字 -->
        <div>
          <div class="tw:font-semibold">
            {{ site.name }}
          </div>
          <div class="tw:text-sm tw:text-gray-500 tw:leading-relaxed">
            {{ site.desc }}
          </div>
        </div>
      </div>
    </el-card>
  </div>
</template>


<script lang="ts" setup>
import {
  HomeFilled,
  DataAnalysis,
  Document,
  Monitor,
  Setting,
  User
} from '@element-plus/icons-vue'

const sites = [
  {
    key: 'main',
    name: '主站',
    desc: '提供统一入口与全站导航服务',
    icon: HomeFilled
  },
  {
    key: 'data',
    name: '数据分析',
    desc: '数据可视化与统计分析平台',
    icon: DataAnalysis
  },
  {
    key: 'docs',
    name: '文档中心',
    desc: '项目文档与使用说明汇总',
    icon: Document
  },
  {
    key: 'monitor',
    name: '监控系统',
    desc: '服务状态与运行指标监控',
    icon: Monitor
  },
  {
    key: 'settings',
    name: '系统配置',
    desc: '系统参数与权限配置管理',
    icon: Setting
  },
  {
    key: 'user',
    name: '用户中心',
    desc: '账号信息与权限管理',
    icon: User
  }
]
</script>

