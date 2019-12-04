
# 1 安装pipenv

```bash
pip3 install pipenv
```

# 2 创建虚拟环境

```bash
# mkdir project
# cd project
# pipenv install // 初始化
```

# 3 安装依赖包

```bash
# pipenv install requests
```

# 4 查看安装包及依赖关系

```bash
# pipenv graph
```

只在开发环境中安装

```bash
# pipenv install --dev requests --three
```

```
--three / --two  Use Python 3/2 when creating virtualenv
```

# 5 兼容requirements.txt文件

```bash
# pipenv lock -r --dev > requirements.txt
```

```bash
# pipenv install -r requirements.txt
```

# 6 运行Python代码

method 1

```bash
# pipenv run python xxx.py
```

method 2

```bash
# pipenv shell
# python3 xxx.py
```
# 7 删除依赖包

```bash
# pipenv uninstall requests
```

# 8 删除虚拟环境

```bash
# pipenv --rm
```

# 9 设置pip源

编辑Pipfile, 修改url的地址



