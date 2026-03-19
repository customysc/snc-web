# SNC寒假WEB开发
本项目使用FastAPi + Vue3 + Mysql开发
# 依赖
*请注意本项目强制要求使用 Python 3.12, 高版本或低版本均可能有问题*
Python 3.12
Node.js 20
# 快速开始
## 前端
换用淘宝源
```shell
npm config set registry http://registry.npmmirror.com
```
建议使用 pnpm
```shell
npm install -g pnpm
```
安装依赖
```shell
pnpm install
```
启动服务
```shell
pnpm run dev
```
## 后端
创建虚拟环境
```shell
python -m venv .venv
```
激活虚拟环境
```shell
.\.venv\scripts\activate
```
安装
```shell
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

配置数据库
复制.env.example文件为.env，再填写配置
启动应用
```shell
fastapi run --reload app/main.py
```

# 规范Git提交
## 关于分支保护
main分支被保护，仅允许branch后，修改再合并，合并前需要代码审查
## Git分支
仅允许使用英文,数字和短横线
格式为：用户名-日期-目的
每人每件事开一个新分支，新分支完成目标并合并后删除
## 提交规范
使用中文编辑提交消息（部分难以用中文表述的专有名词除外）
仅提交代码文件和必要的静态文件
不提交任何下载的包文件，编译的中间或最后结果
保证每次提交的结果可以运行或达成阶段目标
## 合并规范
保证提出合并请求的代码可以运行，并达成目标要求
# 关于前端开发
## 技术栈
框架：Vue3
构建工具：Vite
组件库：ElementPlus
其他Css包：TailWindCSS
## 开发规范
除特殊情况，使用行内样式
仅更改自己负责的文件
