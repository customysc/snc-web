# 快速开始

# Scripts运行方式
## 运行数据库检查
在根目录
```shell
python -m app.backend_pre_start
```
```shell
PYTHONPATH=$(pwd) alembic revision --autogenerate -m "init"
```
```shell
PYTHONPATH=$(pwd) alembic upgrade head
```
```shell
python -m app.initial_data
```