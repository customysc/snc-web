export const currentUser = {
  id: 1,
  name: "张老师",
  avatar: "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
  role: "教师",
  department: "计算机科学与技术学院"
};

export const managedMembers = [
  {
    id: 2,
    name: "李四",
    avatar: "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
    role: "学生",
    department: "计算机科学与技术学院",
    major: "软件工程",
    grade: "大三"
  },
  {
    id: 3,
    name: "王五",
    avatar: "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
    role: "学生",
    department: "计算机科学与技术学院",
    major: "人工智能",
    grade: "大二"
  },
  {
    id: 4,
    name: "赵六",
    avatar: "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
    role: "学生",
    department: "计算机科学与技术学院",
    major: "数据科学",
    grade: "大四"
  }
];

export const followingMembers = [
  {
    id: 5,
    name: "孙七",
    avatar: "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
    role: "教师",
    department: "信息工程学院"
  },
  {
    id: 6,
    name: "周八",
    avatar: "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
    role: "学生",
    department: "计算机科学与技术学院",
    major: "网络工程",
    grade: "大一"
  }
];

export const okrData = [
  {
    id: 1,
    objective: "提升课程教学质量，提高学生满意度",
    owner: "张老师",
    ownerId: 1,
    createdDate: "2026-01-15",
    participants: [
      {
        id: 1,
        name: "张老师",
        avatar: "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
        role: "课程负责人",
        tasks: [
          {
            id: 101,
            title: "更新课程教案和课件，融入最新技术趋势",
            progress: 85,
            subtasks: [
              { id: 1011, title: "更新前端开发课程教案", progress: 90 },
              { id: 1012, title: "制作React技术专题课件", progress: 80 },
              { id: 1013, title: "添加最新前端框架案例", progress: 85 }
            ]
          },
          {
            id: 102,
            title: "设计并实施3个综合性实验项目",
            progress: 70,
            subtasks: [
              { id: 1021, title: "设计前端框架应用实验", progress: 80 },
              { id: 1022, title: "设计后端API开发实验", progress: 75 },
              { id: 1023, title: "设计全栈项目实验", progress: 55 }
            ]
          },
          {
            id: 103,
            title: "建立学生反馈机制，每周收集并响应反馈",
            progress: 90,
            subtasks: [
              { id: 1031, title: "设计反馈问卷模板", progress: 100 },
              { id: 1032, title: "建立反馈收集渠道", progress: 95 },
              { id: 1033, title: "制定反馈响应流程", progress: 85 }
            ]
          },
          {
            id: 104,
            title: "组织4次行业专家讲座",
            progress: 60,
            subtasks: [
              { id: 1041, title: "联系互联网公司技术专家", progress: 70 },
              { id: 1042, title: "安排讲座场地和时间", progress: 80 },
              { id: 1043, title: "组织学生参与和反馈", progress: 50 }
            ]
          }
        ]
      },
      {
        id: 2,
        name: "李四",
        avatar: "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
        role: "学生助教",
        tasks: [
          {
            id: 201,
            title: "协助设计并实施3个综合性实验项目",
            progress: 75,
            subtasks: [
              { id: 2011, title: "协助准备实验材料", progress: 85 },
              { id: 2012, title: "指导学生实验操作", progress: 70 },
              { id: 2013, title: "批改实验报告", progress: 75 }
            ]
          },
          {
            id: 202,
            title: "收集学生反馈并整理报告",
            progress: 85,
            subtasks: [
              { id: 2021, title: "分发反馈问卷", progress: 100 },
              { id: 2022, title: "整理反馈数据", progress: 80 },
              { id: 2023, title: "撰写反馈分析报告", progress: 85 }
            ]
          },
          {
            id: 203,
            title: "协助组织行业专家讲座",
            progress: 65,
            subtasks: [
              { id: 2031, title: "协助联系讲座嘉宾", progress: 70 },
              { id: 2032, title: "准备讲座场地布置", progress: 75 },
              { id: 2033, title: "组织学生签到和入场", progress: 60 }
            ]
          }
        ]
      },
      {
        id: 6,
        name: "周八",
        avatar: "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
        role: "学生代表",
        tasks: [
          {
            id: 601,
            title: "收集学生课程满意度反馈",
            progress: 90,
            subtasks: [
              { id: 6011, title: "在班级群收集反馈", progress: 95 },
              { id: 6012, title: "组织学生座谈会", progress: 85 },
              { id: 6013, title: "整理满意度数据", progress: 90 }
            ]
          },
          {
            id: 602,
            title: "协助建立学生反馈机制",
            progress: 80,
            subtasks: [
              { id: 6021, title: "调研其他课程反馈机制", progress: 85 },
              { id: 6022, title: "提出反馈机制改进建议", progress: 75 },
              { id: 6023, title: "协助制定反馈流程", progress: 80 }
            ]
          }
        ]
      }
    ],
    keyResults: [
      {
        id: 1,
        title: "更新课程教案和课件，融入最新技术趋势",
        progress: 85,
        weight: 30,
        score: 3.8,
        status: 'normal'
      },
      {
        id: 2,
        title: "设计并实施3个综合性实验项目",
        progress: 70,
        weight: 25,
        score: 3.5,
        status: 'normal'
      },
      {
        id: 3,
        title: "建立学生反馈机制，每周收集并响应反馈",
        progress: 90,
        weight: 20,
        score: 4.0,
        status: 'normal'
      },
      {
        id: 4,
        title: "组织4次行业专家讲座",
        progress: 60,
        weight: 15,
        score: 3.0,
        status: 'normal'
      },
      {
        id: 5,
        title: "提升学生课程满意度至4.8分以上",
        progress: 75,
        weight: 10,
        score: 3.7,
        status: 'normal'
      }
    ],
    totalProgress: 76,
    totalScore: 3.6
  },
  {
    id: 2,
    objective: "指导学生团队完成科研项目，发表学术论文",
    owner: "张老师",
    ownerId: 1,
    createdDate: "2026-01-10",
    participants: [
      {
        id: 1,
        name: "张老师",
        avatar: "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
        role: "项目指导",
        tasks: [
          {
            id: 301,
            title: "指导学生团队完成科研项目",
            progress: 80,
            subtasks: [
              { id: 3011, title: "制定项目研究计划", progress: 100 },
              { id: 3012, title: "定期指导项目进展", progress: 75 },
              { id: 3013, title: "解决项目关键问题", progress: 85 }
            ]
          },
          {
            id: 302,
            title: "指导论文撰写和修改",
            progress: 50,
            subtasks: [
              { id: 3021, title: "确定论文研究方向", progress: 100 },
              { id: 3022, title: "指导论文大纲撰写", progress: 70 },
              { id: 3023, title: "修改论文初稿", progress: 30 }
            ]
          },
          {
            id: 303,
            title: "协助申请软件著作权",
            progress: 65,
            subtasks: [
              { id: 3031, title: "准备软件著作权申请材料", progress: 80 },
              { id: 3032, title: "整理软件文档", progress: 60 },
              { id: 3033, title: "提交申请材料", progress: 55 }
            ]
          }
        ]
      },
      {
        id: 3,
        name: "王五",
        avatar: "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
        role: "项目组长",
        tasks: [
          {
            id: 401,
            title: "完成基于机器学习的学生行为分析系统",
            progress: 80,
            subtasks: [
              { id: 4011, title: "设计系统架构", progress: 90 },
              { id: 4012, title: "实现数据采集模块", progress: 85 },
              { id: 4013, title: "开发机器学习模型", progress: 75 },
              { id: 4014, title: "系统测试和优化", progress: 70 }
            ]
          },
          {
            id: 402,
            title: "撰写学术论文初稿",
            progress: 50,
            subtasks: [
              { id: 4021, title: "收集相关研究文献", progress: 90 },
              { id: 4022, title: "分析实验数据", progress: 70 },
              { id: 4023, title: "撰写论文主体部分", progress: 40 },
              { id: 4024, title: "完善论文参考文献", progress: 50 }
            ]
          },
          {
            id: 403,
            title: "组织团队会议和进度汇报",
            progress: 90,
            subtasks: [
              { id: 4031, title: "制定会议议程", progress: 100 },
              { id: 4032, title: "主持团队会议", progress: 95 },
              { id: 4033, title: "整理会议纪要", progress: 85 },
              { id: 4034, title: "跟踪任务执行情况", progress: 90 }
            ]
          }
        ]
      },
      {
        id: 4,
        name: "赵六",
        avatar: "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
        role: "核心成员",
        tasks: [
          {
            id: 501,
            title: "协助开发机器学习系统",
            progress: 85,
            subtasks: [
              { id: 5011, title: "协助数据预处理", progress: 90 },
              { id: 5012, title: "实现特征工程", progress: 85 },
              { id: 5013, title: "协助模型训练和评估", progress: 80 }
            ]
          },
          {
            id: 502,
            title: "收集和整理实验数据",
            progress: 90,
            subtasks: [
              { id: 5021, title: "设计数据收集方案", progress: 100 },
              { id: 5022, title: "收集学生行为数据", progress: 95 },
              { id: 5023, title: "数据清洗和整理", progress: 85 }
            ]
          },
          {
            id: 503,
            title: "协助论文撰写",
            progress: 45,
            subtasks: [
              { id: 5031, title: "协助文献综述", progress: 70 },
              { id: 5032, title: "撰写实验方法部分", progress: 50 },
              { id: 5033, title: "整理实验结果图表", progress: 40 }
            ]
          }
        ]
      },
      {
        id: 5,
        name: "孙七",
        avatar: "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
        role: "技术顾问",
        tasks: [
          {
            id: 601,
            title: "提供技术支持和指导",
            progress: 75,
            subtasks: [
              { id: 6011, title: "提供机器学习技术咨询", progress: 80 },
              { id: 6012, title: "指导系统架构设计", progress: 70 },
              { id: 6013, title: "评审技术方案", progress: 80 }
            ]
          },
          {
            id: 602,
            title: "协助解决技术难题",
            progress: 65,
            subtasks: [
              { id: 6021, title: "分析技术难点", progress: 85 },
              { id: 6022, title: "提供解决方案", progress: 60 },
              { id: 6023, title: "验证解决方案有效性", progress: 55 }
            ]
          }
        ]
      }
    ],
    keyResults: [
      {
        id: 1,
        title: "完成基于机器学习的学生行为分析系统",
        progress: 80,
        weight: 30,
        score: 3.8,
        status: 'normal'
      },
      {
        id: 2,
        title: "撰写并投稿2篇学术论文",
        progress: 50,
        weight: 30,
        score: 2.5,
        status: 'normal'
      },
      {
        id: 3,
        title: "申请1项软件著作权",
        progress: 65,
        weight: 20,
        score: 3.2,
        status: 'normal'
      },
      {
        id: 4,
        title: "参加1次学术会议并做报告",
        progress: 40,
        weight: 20,
        score: 2.0,
        status: 'normal'
      }
    ],
    totalProgress: 59,
    totalScore: 2.9
  },
  {
    id: 3,
    objective: "加强校企合作，为学生提供更多实践机会",
    owner: "张老师",
    ownerId: 1,
    participants: [
      {
        id: 1,
        name: "张老师",
        avatar: "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
        role: "合作协调",
        tasks: [
          {
            id: 701,
            title: "与企业建立合作关系",
            progress: 70,
            subtasks: [
              { id: 7011, title: "调研潜在合作企业", progress: 80 },
              { id: 7012, title: "联系企业负责人", progress: 75 },
              { id: 7013, title: "洽谈合作意向", progress: 65 }
            ]
          },
          {
            id: 702,
            title: "协调校企合作项目",
            progress: 60,
            subtasks: [
              { id: 7021, title: "制定合作项目计划", progress: 70 },
              { id: 7022, title: "协调项目资源", progress: 60 },
              { id: 7023, title: "监督项目执行", progress: 55 }
            ]
          },
          {
            id: 703,
            title: "监督实践基地建设",
            progress: 50,
            subtasks: [
              { id: 7031, title: "制定实践基地建设标准", progress: 60 },
              { id: 7032, title: "审核实践基地建设方案", progress: 50 },
              { id: 7033, title: "验收实践基地", progress: 40 }
            ]
          }
        ]
      },
      {
        id: 5,
        name: "孙七",
        avatar: "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
        role: "企业联络",
        tasks: [
          {
            id: 801,
            title: "联系企业建立合作关系",
            progress: 75,
            subtasks: [
              { id: 8011, title: "收集企业信息", progress: 85 },
              { id: 8012, title: "联系企业HR", progress: 80 },
              { id: 8013, title: "安排企业拜访", progress: 70 }
            ]
          },
          {
            id: 802,
            title: "组织企业参观和技术分享会",
            progress: 85,
            subtasks: [
              { id: 8021, title: "联系企业安排参观", progress: 90 },
              { id: 8022, title: "组织学生报名", progress: 85 },
              { id: 8023, title: "协调技术分享会", progress: 80 }
            ]
          },
          {
            id: 803,
            title: "协调实习岗位",
            progress: 65,
            subtasks: [
              { id: 8031, title: "收集企业实习需求", progress: 75 },
              { id: 8032, title: "推荐学生实习", progress: 65 },
              { id: 8033, title: "跟进实习情况", progress: 60 }
            ]
          }
        ]
      },
      {
        id: 4,
        name: "赵六",
        avatar: "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
        role: "学生代表",
        tasks: [
          {
            id: 901,
            title: "收集学生实习需求",
            progress: 90,
            subtasks: [
              { id: 9011, title: "设计实习需求问卷", progress: 95 },
              { id: 9012, title: "收集学生反馈", progress: 90 },
              { id: 9013, title: "整理需求报告", progress: 85 }
            ]
          },
          {
            id: 902,
            title: "协助组织企业参观活动",
            progress: 80,
            subtasks: [
              { id: 9021, title: "宣传企业参观活动", progress: 85 },
              { id: 9022, title: "组织学生报名", progress: 80 },
              { id: 9023, title: "协助活动执行", progress: 75 }
            ]
          }
        ]
      }
    ],
    keyResults: [
      {
        id: 1,
        title: "与5家IT企业建立合作关系",
        progress: 70,
        weight: 30,
        score: 3.5,
        status: 'normal'
      },
      {
        id: 2,
        title: "建立3个校外实践基地",
        progress: 50,
        weight: 25,
        score: 2.5,
        status: 'normal'
      },
      {
        id: 3,
        title: "组织2次企业参观和技术分享会",
        progress: 80,
        weight: 20,
        score: 4.0,
        status: 'normal'
      },
      {
        id: 4,
        title: "为学生提供20个实习岗位",
        progress: 60,
        weight: 25,
        score: 3.0,
        status: 'normal'
      }
    ],
    totalProgress: 65,
    totalScore: 3.2
  },
  {
    id: 4,
    objective: "提升个人编程能力，完成课程项目",
    owner: "李四",
    ownerId: 2,
    parentObjective: "提升课程教学质量，提高学生满意度",
    parentOwner: "张老师",
    participants: [
      {
        id: 2,
        name: "李四",
        avatar: "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
        role: "项目负责人",
        tasks: [
          {
            id: 1001,
            title: "学习并掌握React框架",
            progress: 90,
            subtasks: [
              { id: 10011, title: "学习React基础概念", progress: 100 },
              { id: 10012, title: "掌握组件开发", progress: 95 },
              { id: 10013, title: "学习状态管理", progress: 85 },
              { id: 10014, title: "掌握路由配置", progress: 90 }
            ]
          },
          {
            id: 1002,
            title: "完成个人博客网站开发",
            progress: 75,
            subtasks: [
              { id: 10021, title: "设计网站架构", progress: 90 },
              { id: 10022, title: "开发前端页面", progress: 80 },
              { id: 10023, title: "实现博客功能", progress: 70 },
              { id: 10024, title: "优化用户体验", progress: 65 }
            ]
          },
          {
            id: 1003,
            title: "撰写项目文档和技术总结",
            progress: 80,
            subtasks: [
              { id: 10031, title: "编写需求文档", progress: 90 },
              { id: 10032, title: "编写技术文档", progress: 85 },
              { id: 10033, title: "撰写技术总结", progress: 75 }
            ]
          },
          {
            id: 1004,
            title: "部署项目到云服务器",
            progress: 60,
            subtasks: [
              { id: 10041, title: "配置服务器环境", progress: 70 },
              { id: 10042, title: "部署前端项目", progress: 65 },
              { id: 10043, title: "配置域名和SSL", progress: 50 }
            ]
          }
        ]
      },
      {
        id: 6,
        name: "周八",
        avatar: "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
        role: "技术助手",
        tasks: [
          {
            id: 1101,
            title: "协助学习React框架",
            progress: 85,
            subtasks: [
              { id: 11011, title: "分享学习资料", progress: 90 },
              { id: 11012, title: "解答技术问题", progress: 85 },
              { id: 11013, title: "一起练习项目", progress: 80 }
            ]
          },
          {
            id: 1102,
            title: "协助完成网站开发",
            progress: 70,
            subtasks: [
              { id: 11021, title: "协助代码审查", progress: 75 },
              { id: 11022, title: "协助调试问题", progress: 70 },
              { id: 11023, title: "协助功能测试", progress: 65 }
            ]
          },
          {
            id: 1103,
            title: "协助撰写项目文档",
            progress: 75,
            subtasks: [
              { id: 11031, title: "协助整理文档结构", progress: 80 },
              { id: 11032, title: "协助编写技术说明", progress: 75 },
              { id: 11033, title: "协助文档排版", progress: 70 }
            ]
          }
        ]
      }
    ],
    keyResults: [
      {
        id: 1,
        title: "学习并掌握React框架",
        progress: 90,
        weight: 30,
        score: 4.0
      },
      {
        id: 2,
        title: "完成个人博客网站开发",
        progress: 75,
        weight: 40,
        score: 3.5
      },
      {
        id: 3,
        title: "撰写项目文档和技术总结",
        progress: 80,
        weight: 30,
        score: 4.0
      },
      {
        id: 4,
        title: "部署项目到云服务器",
        progress: 60,
        weight: 20,
        score: 3.0
      }
    ],
    totalProgress: 76,
    totalScore: 3.6
  },
  {
    id: 5,
    objective: "提高专业成绩，获得奖学金",
    owner: "王五",
    ownerId: 3,
    participants: [
      {
        id: 3,
        name: "王五",
        avatar: "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
        role: "学生",
        tasks: [
          {
            id: 1201,
            title: "专业课程平均分达到90分以上",
            progress: 85,
            subtasks: [
              { id: 12011, title: "学习数据结构课程", progress: 90 },
              { id: 12012, title: "学习算法设计课程", progress: 85 },
              { id: 12013, title: "学习数据库原理课程", progress: 88 },
              { id: 12014, title: "学习操作系统课程", progress: 82 }
            ]
          },
          {
            id: 1202,
            title: "完成2篇课程论文",
            progress: 70,
            subtasks: [
              { id: 12021, title: "确定论文选题", progress: 100 },
              { id: 12022, title: "收集文献资料", progress: 85 },
              { id: 12023, title: "撰写论文初稿", progress: 65 },
              { id: 12024, title: "修改和完善论文", progress: 50 }
            ]
          },
          {
            id: 1203,
            title: "参加1次学科竞赛并获奖",
            progress: 60,
            subtasks: [
              { id: 12031, title: "选择竞赛项目", progress: 100 },
              { id: 12032, title: "准备竞赛作品", progress: 70 },
              { id: 12033, title: "参加竞赛答辩", progress: 40 }
            ]
          }
        ]
      },
      {
        id: 1,
        name: "张老师",
        avatar: "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
        role: "导师",
        tasks: [
          {
            id: 1301,
            title: "指导课程学习",
            progress: 90,
            subtasks: [
              { id: 13011, title: "解答课程疑问", progress: 95 },
              { id: 13012, title: "推荐学习资料", progress: 90 },
              { id: 13013, title: "指导学习方法", progress: 85 }
            ]
          },
          {
            id: 1302,
            title: "指导论文写作",
            progress: 75,
            subtasks: [
              { id: 13021, title: "指导论文选题", progress: 100 },
              { id: 13022, title: "指导文献综述", progress: 80 },
              { id: 13023, title: "修改论文内容", progress: 60 }
            ]
          },
          {
            id: 1303,
            title: "推荐学科竞赛",
            progress: 85,
            subtasks: [
              { id: 13031, title: "推荐合适竞赛", progress: 100 },
              { id: 13032, title: "指导竞赛准备", progress: 80 },
              { id: 13033, title: "提供技术支持", progress: 75 }
            ]
          }
        ]
      }
    ],
    keyResults: [
      {
        id: 1,
        title: "专业课程平均分达到90分以上",
        progress: 85,
        weight: 40,
        score: 3.8,
        status: 'normal'
      },
      {
        id: 2,
        title: "完成2篇课程论文",
        progress: 70,
        weight: 30,
        score: 3.5,
        status: 'normal'
      },
      {
        id: 3,
        title: "参加1次学科竞赛并获奖",
        progress: 60,
        weight: 30,
        score: 3.0,
        status: 'normal'
      }
    ],
    totalProgress: 72,
    totalScore: 3.4
  },
  {
    id: 6,
    objective: "准备毕业设计和就业规划",
    owner: "赵六",
    ownerId: 4,
    participants: [
      {
        id: 4,
        name: "赵六",
        avatar: "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
        role: "学生",
        tasks: [
          {
            id: 1401,
            title: "确定毕业设计选题并完成开题报告",
            progress: 90,
            subtasks: [
              { id: 14011, title: "调研毕业设计方向", progress: 100 },
              { id: 14012, title: "确定毕业设计选题", progress: 100 },
              { id: 14013, title: "撰写开题报告", progress: 90 },
              { id: 14014, title: "完成开题答辩", progress: 85 }
            ]
          },
          {
            id: 1402,
            title: "完成简历制作和面试准备",
            progress: 75,
            subtasks: [
              { id: 14021, title: "整理个人经历", progress: 100 },
              { id: 14022, title: "制作专业简历", progress: 85 },
              { id: 14023, title: "准备面试常见问题", progress: 75 },
              { id: 14024, title: "进行模拟面试", progress: 65 }
            ]
          },
          {
            id: 1403,
            title: "投递10家企业并获得3个面试机会",
            progress: 60,
            subtasks: [
              { id: 14031, title: "筛选目标企业", progress: 80 },
              { id: 14032, title: "投递简历", progress: 70 },
              { id: 14033, title: "跟进面试邀请", progress: 50 },
              { id: 14034, title: "准备面试", progress: 45 }
            ]
          },
          {
            id: 1404,
            title: "完成毕业设计初稿",
            progress: 40,
            subtasks: [
              { id: 14041, title: "完成需求分析", progress: 60 },
              { id: 14042, title: "完成系统设计", progress: 50 },
              { id: 14043, title: "完成代码开发", progress: 40 },
              { id: 14044, title: "撰写毕业论文", progress: 30 }
            ]
          }
        ]
      },
      {
        id: 1,
        name: "张老师",
        avatar: "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
        role: "毕设导师",
        tasks: [
          {
            id: 1501,
            title: "指导毕业设计选题",
            progress: 100,
            subtasks: [
              { id: 15011, title: "提供选题建议", progress: 100 },
              { id: 15012, title: "审核选题方向", progress: 100 },
              { id: 15013, title: "指导开题报告", progress: 95 }
            ]
          },
          {
            id: 1502,
            title: "指导开题报告写作",
            progress: 95,
            subtasks: [
              { id: 15021, title: "审阅开题报告", progress: 100 },
              { id: 15022, title: "提出修改意见", progress: 95 },
              { id: 15023, title: "指导开题答辩", progress: 90 }
            ]
          },
          {
            id: 1503,
            title: "指导毕业设计开发",
            progress: 50,
            subtasks: [
              { id: 15031, title: "指导系统设计", progress: 70 },
              { id: 15032, title: "指导代码开发", progress: 50 },
              { id: 15033, title: "解决技术问题", progress: 40 }
            ]
          }
        ]
      },
      {
        id: 5,
        name: "孙七",
        avatar: "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",
        role: "就业指导",
        tasks: [
          {
            id: 1601,
            title: "指导简历制作",
            progress: 90,
            subtasks: [
              { id: 16011, title: "提供简历模板", progress: 100 },
              { id: 16012, title: "指导简历内容", progress: 90 },
              { id: 16013, title: "修改简历格式", progress: 85 }
            ]
          },
          {
            id: 1602,
            title: "提供面试技巧培训",
            progress: 85,
            subtasks: [
              { id: 16021, title: "讲解面试流程", progress: 100 },
              { id: 16022, title: "分享面试技巧", progress: 85 },
              { id: 16023, title: "进行模拟面试", progress: 80 }
            ]
          },
          {
            id: 1603,
            title: "推荐就业机会",
            progress: 75,
            subtasks: [
              { id: 16031, title: "收集招聘信息", progress: 90 },
              { id: 16032, title: "推荐合适岗位", progress: 80 },
              { id: 16033, title: "提供内推机会", progress: 65 }
            ]
          }
        ]
      }
    ],
    keyResults: [
      {
        id: 1,
        title: "确定毕业设计选题并完成开题报告",
        progress: 90,
        weight: 30,
        score: 4.0,
        status: 'normal'
      },
      {
        id: 2,
        title: "完成简历制作和面试准备",
        progress: 75,
        weight: 25,
        score: 3.5,
        status: 'normal'
      },
      {
        id: 3,
        title: "投递10家企业并获得3个面试机会",
        progress: 60,
        weight: 25,
        score: 3.0,
        status: 'normal'
      },
      {
        id: 4,
        title: "完成毕业设计初稿",
        progress: 40,
        weight: 20,
        score: 2.0,
        status: 'normal'
      }
    ],
    totalProgress: 66,
    totalScore: 3.1
  }
];
