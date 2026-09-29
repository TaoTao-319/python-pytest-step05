# Python Testing Practice

这是第 2 个月第 1 周的 Python 基础练习项目，重点练习变量、字符串、列表、字典、条件判断、循环、函数、类型判断、异常处理和基础数据校验。

## 项目文件

| 文件 | 功能 |
| --- | --- |
| `basic_syntax.py` | 练习变量、字符串、列表、字典、`if`、`for` 和函数 |
| `phone_validator.py` | 校验手机号格式，并演示多种输入情况 |
| `password_validator.py` | 校验密码长度、大小写字母、数字、特殊字符和空格 |
| `shopping_cart.py` | 校验购物车商品数据并计算购物车总价 |
| `demo.py` | 统一演示手机号、密码和购物车三个业务场景 |

## 环境要求

- Python 3
- 不依赖第三方 Python 库

## 运行方式

在当前目录打开终端，分别运行：

```bash
python basic_syntax.py
python phone_validator.py
python password_validator.py
python shopping_cart.py
python demo.py
```

如果只想查看整合后的主要演示，可以运行：

```bash
python demo.py
```

## 主要练习内容

### 基础语法

`basic_syntax.py` 包含：

- 字符串、数字和布尔值
- 列表的添加和修改
- 字典中键和值的读取
- `if` 条件判断
- `for` 循环
- 函数定义与调用
- 总分和平均分计算

### 手机号校验

`phone_validator.py` 按以下规则校验手机号：

- 必须是字符串
- 必须是 11 位
- 必须全部由数字组成
- 必须以 `1` 开头
- 第二位必须是 `3`、`4`、`5`、`6`、`7`、`8` 或 `9`

### 密码校验

`password_validator.py` 检查：

- 密码长度为 8—20 位
- 至少包含一个大写字母
- 至少包含一个小写字母
- 至少包含一个数字
- 至少包含一个特殊字符
- 不能包含空格

函数会返回总体结果和错误列表，多个错误可以一次性返回。

### 购物车校验

`shopping_cart.py` 检查：

- 购物车是否为列表
- 商品是否为字典
- 商品是否包含 `name`、`price` 和 `quantity`
- 商品名称是否为空
- 价格是否为有效数字且不小于 0
- 数量是否为整数且不小于 0
- `True` 和 `False` 不被当作价格或数量

示例数据覆盖正常购物车、空购物车、多个商品、第二个商品错误、第三个商品错误、字段缺失、错误类型、负数、空名称和异常输入等情况。

## 当前项目特点

- 使用提前返回处理明显的输入错误
- 使用 `try...except` 捕获 `ValueError`
- 使用 `enumerate` 标记购物车中的商品编号
- 使用 `round(total, 2)` 保留购物车总价两位小数
- 使用 f-string 格式化输出

## 后续学习方向

下一步可以使用 pytest 为手机号校验、密码校验和购物车计算函数补充自动化测试。
