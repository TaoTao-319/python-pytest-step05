# 手机号校验

def is_valid_phone(phone):
    """判断输入是否符合本练习设定的中国大陆手机号规则。

    规则：
    1. 必须是字符串；
    2. 必须是 11 位；
    3. 必须全部由数字组成；
    4. 第一位必须是 1；
    5. 第二位必须是 3、4、5、6、7、8 或 9。
    """
    if not isinstance(phone, str):
        return False
    if len(phone) != 11:
        return False
    if not phone.isdigit():
        return False
    if not phone.startswith("1"):
        return False
    return phone[1] in "3456789"


def explain_phone_result(phone):
    """返回更适合展示给用户的校验结果。"""
    if is_valid_phone(phone):
        return f"手机号 {phone} 有效。"
    return f"手机号 {phone!r} 无效，请检查格式。"


def main():
    examples = [
        "13812345678",
        "15900001111",
        "12345678901",
        "1381234567",
        "138123456789",
        "1381234567a",
        "",
        None,
        13812345678,
    ]

    for phone in examples:
        print(explain_phone_result(phone))


if __name__ == "__main__":
    main()
