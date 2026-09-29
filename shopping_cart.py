# 购物车总价计算

def validate_cart_item(item):
    """校验单个商品，并返回错误列表。"""
    errors = []

    if not isinstance(item, dict):
        return ["商品必须是字典"]

    for field in ("name", "price", "quantity"):
        if field not in item:
            errors.append(f"商品缺少字段：{field}")

    if errors:
        return errors

    if not isinstance(item["name"], str) or not item["name"].strip():
        errors.append("商品名称必须是非空字符串")
    # strip() 会把开头和结尾连续的空格全部去掉
    if not isinstance(item["price"], (int, float)) or isinstance(item["price"], bool):
        errors.append("商品价格必须是数字")
    # Python 中 bool 是 int 的子类型，所以 isinstance(True, int) 的结果是 True
    # 如果不单独排除 bool，True 可能被当成价格 1，False 可能被当成价格 0
    # 价格应该是真正的整数或小数，因此这里要排除 True 和 False
    elif item["price"] < 0:
        errors.append("商品价格不能小于 0")
    if not isinstance(item["quantity"], int) or isinstance(item["quantity"], bool):
        errors.append("商品数量必须是整数")
    elif item["quantity"] < 0:
        errors.append("商品数量不能小于 0")

    return errors


def calculate_total(cart):
    """计算购物车总价。

    空购物车返回 0.0；发现数据错误时抛出 ValueError，并说明原因。
    """
    if not isinstance(cart, list):
        raise ValueError("购物车必须是列表")

    total = 0.0
    for index, item in enumerate(cart, start=1):
        errors = validate_cart_item(item)
        if errors:
            raise ValueError(f"第 {index} 个商品数据无效：" + "；".join(errors))
        total += item["price"] * item["quantity"]

    return round(total, 2)  # 把 total 四舍五入并保留两位小数


def try_calculate(cart):
    """安全执行总价计算，方便演示异常输入。"""
    try:
        # 先执行 try 中的代码
        total = calculate_total(cart)
        print(f"计算成功，总价：{total:.2f} 元")
        # {total:.2f} 中的冒号是 f-string 中的格式说明符分隔符
        # .2f 表示以小数形式显示 total，并保留两位小数
    except ValueError as error:
        # 如果没有异常，就跳过 except；如果出现 ValueError，就跳过 try 剩余代码并执行这里
        print(f"计算失败：{error}")


def main():
    normal_cart = [
        {"name": "鼠标", "price": 99.0, "quantity": 2},
        {"name": "键盘", "price": 199.0, "quantity": 1},
    ]

    examples = [
        # 正常情况：多个商品，检查总价是否能够正确累加
        [
            {"name": "耳机", "price": 129.9, "quantity": 1},
            {"name": "鼠标垫", "price": 29.9, "quantity": 2},
            {"name": "USB线", "price": 19.5, "quantity": 3},
        ],
        normal_cart,
        # 第 2 个商品出错：验证错误提示中的商品编号
        [
            {"name": "鼠标", "price": 99, "quantity": 1},
            {"name": "键盘", "price": 199, "quantity": -1},
            {"name": "显示器", "price": 899, "quantity": 1},
        ],
        # 第 3 个商品出错：前两个商品有效，第三个商品价格类型错误
        [
            {"name": "鼠标", "price": 99, "quantity": 1},
            {"name": "键盘", "price": 199, "quantity": 1},
            {"name": "显示器", "price": "899", "quantity": 1},
        ],
        [],
        [{"name": "优惠商品", "price": 10, "quantity": 0}],
        [{"name": "负价格商品", "price": -10, "quantity": 1}],
        [{"name": "负数量商品", "price": 10, "quantity": -1}],
        [{"name": "缺少价格", "quantity": 1}],
        [{"price": 99, "quantity": 1}],
        [{"name": "缺少数量", "price": 99}],
        [{"name": "价格是字符串", "price": "99", "quantity": 1}],
        [{"name": "价格是布尔值", "price": True, "quantity": 1}],
        [{"name": "数量是小数", "price": 99, "quantity": 1.5}],
        [{"name": "数量是布尔值", "price": 99, "quantity": False}],
        [{"name": "", "price": 99, "quantity": 1}],
        [{"name": "   ", "price": 99, "quantity": 1}],
        ["不是商品字典"],
        "不是购物车列表",
    ]

    for cart in examples:
        print(f"购物车：{cart}")
        try_calculate(cart)
        print("=" * 30)


if __name__ == "__main__":
    main()
