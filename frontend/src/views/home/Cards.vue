<template>
  <div :style="{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '16px' }">
    <el-card
      v-for="site in sites"
      :key="site.key"
      shadow="hover"
      :style="{ cursor: 'pointer' }"
      @click="goTo(site.url)"
    >
      <div :style="{ display: 'flex', alignItems: 'flex-start', gap: '16px' }">
        <el-icon :size="40">
          <component :is="site.icon" />
        </el-icon>
        <div>
          <div :style="{ fontWeight: '600' }">{{ site.name }}</div>
          <div :style="{ fontSize: '12px', color: '#666', lineHeight: '1.5' }">
            {{ site.desc }}
          </div>
        </div>
      </div>
    </el-card>
  </div>

  <el-card shadow="never" :body-style="{ padding: '20px' }">
    <div :style="{ fontWeight: '700', fontSize: '18px', marginBottom: '20px', textAlign: 'center' }">
      <el-icon :size="20" :style="{ marginRight: '8px' }"></el-icon>
      校内网站导航
    </div>

    <el-tabs v-model="activeTab" type="card" :stretch="true">
      <el-tab-pane v-for="(category, index) in navCategories" :key="index" :label="category.name" :name="category.name">
        <div :style="{ display: 'flex', flexWrap: 'wrap', gap: '12px', padding: '10px 0' }">
          <el-tag
            v-for="link in category.links"
            :key="link.name"
            type="info"
            :style="{ cursor: 'pointer', fontSize: '14px', padding: '8px 16px', borderRadius: '4px' }"
            @click="goTo(link.url)"
          >
            {{ link.name }}
          </el-tag>
        </div>
      </el-tab-pane>
    </el-tabs>
  </el-card>

</template>

<script lang="ts" setup>
import { HomeFilled, DataAnalysis, Document, Monitor, Setting, User, Link } from '@element-plus/icons-vue'

const sites = [
  {
    key: 'main',
    name: '主站',
    desc: '提供统一入口与全站导航服务',
    icon: HomeFilled,
  },
  {
    key: 'data',
    name: '数据分析',
    desc: '数据可视化与统计分析平台',
    icon: DataAnalysis,
  },
  {
    key: 'docs',
    name: '文档中心',
    desc: '项目文档与使用说明汇总',
    icon: Document,
  },
  {
    key: 'monitor',
    name: '监控系统',
    desc: '服务状态与运行指标监控',
    icon: Monitor,
  },
  {
    key: 'settings',
    name: '系统配置',
    desc: '系统参数与权限配置管理',
    icon: Setting,
  },
  {
    key: 'user',
    name: '用户中心',
    desc: '账号信息与权限管理',
    icon: User,
  },
]

const goTo = (url: string) => {
  if (url) {
    window.open(url, '_blank') 
  }
}

import { ref } from 'vue';


const navCategories = ref([
  {
    name: '部门网站',
    links: [
      { name: '北京化工大学首页', url: 'https://www.buct.edu.cn' },
      { name: '校长办公室', url: 'https://xb.buct.edu.cn/main.htm' },
      { name: '学生工作办公室', url: 'https://xgb.buct.edu.cn/main.htm' },
      { name: '图书馆', url: 'https://tsg.buct.edu.cn/main.htm' },
      { name: '财务处', url: 'https://cwc.buct.edu.cn/main.htm' },
      { name: '人事处', url: 'https://rsc.buct.edu.cn/main.htm' },
    ]
  },
  {
    name: '学院网站',
    links: [
      { name: '信息学院', url: 'https://cist.buct.edu.cn/main.htm' },
      { name: '化工学院', url: 'https://chem.buct.edu.cn/main.htm' },
      { name: '机电学院', url: 'https://mech.buct.edu.cn/main.htm' },
      { name: '材料学院', url: 'https://cmse.buct.edu.cn/main.htm' },
    ]
  },
  {
    name: '应用系统',
    links: [
      { name: '教务系统', url: 'https://experimental-auth-endpoint.buct.edu.cn/?timestamp=1769501391470&service=https%3A%2F%2Fjwglxt.buct.edu.cn%2Fsso%2Fjziotlogin' },
      { name: '学生资助', url: 'https://zizhu.buct.edu.cn/main.htm' },
      { name: 'VPN', url: 'https://vpn.buct.edu.cn/main.htm' },
    ]
  },
  {
    name: '平台资源',
    links: [
      { name: '图书馆资源', url: 'https://tsg.buct.edu.cn/main.htm' },
      { name: '综合教学服务平台', url: 'https://sjcx.buct.edu.cn/#/login' },
    ]
  }
]);

const activeTab = ref('部门网站'); 

</script>