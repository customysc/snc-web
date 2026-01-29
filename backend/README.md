# 介绍
本项目使用 FastApi 构建
ORM: SQLAlchemy 2.0

# 快速开始
安装依赖
```shell
uv sync
```
配置数据库
复制.env.example文件为.env，再填写配置
启动应用
```shell
fastapi run --reload app/main.py
```

# alembic 数据库迁移
在根目录
```shell
PYTHONPATH=$(pwd) alembic revision --autogenerate -m "{your_message}"
```
```shell
PYTHONPATH=$(pwd) alembic upgrade head
```