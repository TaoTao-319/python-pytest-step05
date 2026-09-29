# 密码规则校验

def validate_password(password):
    """检查密码是否符合规则，并返回总体结果和具体错误。

    密码规则：长度 8—20 位，包含大小写字母、数字和特殊字符，且不能有空格。
    """
    errors = []

    if not isinstance(password, str):
        return {"valid": False, "errors": ["密码必须是字符串"]}

    if not 8 <= len(password) <= 20:
        errors.append("密码长度必须在 8 到 20 位之间")
    if " " in password:
        errors.append("密码不能包含空格")
    if not any(character.isupper() for character in password):
        errors.append("密码至少需要一个大写字母")
    # for character in password：逐个读取密码中的字符
    # character.isupper()：判断当前字符是不是大写字母
    # any(...)：只要有一个字符是大写字母，就返回 True
    if not any(character.islower() for character in password):
        errors.append("密码至少需要一个小写字母")
    if not any(character.isdigit() for character in password):
        errors.append("密码至少需要一个数字")
    if not any(not character.isalnum() and not character.isspace() for character in password):
        errors.append("密码至少需要一个特殊字符")
    # character.isalnum()：判断字符是否是字母或数字
    # character.isspace()：判断字符是否是空格或其他空白字符
    # not character.isalnum() and not character.isspace()：判断字符是否是特殊字符

    return {
        "valid": not errors,
        # errors 是保存错误信息的列表
        # errors = [] 时，空列表会被判断为 False，not errors 的结果是 True，表示密码有效
        # errors = ["缺少数字"] 时，非空列表会被判断为 True，not errors 的结果是 False，表示密码无效
        "errors": errors,
    }


def print_password_result(password):
    """打印密码校验结果，但不打印密码本身。"""
    result = validate_password(password)
    if result["valid"]:
        print("密码校验通过。")
        return

    print("密码校验不通过：")
    for error in result["errors"]:
        print("-", error)


def main():
    examples = [
        "Abc12345!",
        "abc12345!",
        "ABC12345!",
        "Abcdefgh!",
        "Abc123456",
        "Ab1!",
        "Abc 1234!",
        "",
        None,
    ]

    for password in examples:
        print(f"输入长度：{len(password) if isinstance(password, str) else '非字符串'}")
        print_password_result(password)
        print("=" * 30)


if __name__ == "__main__":
    main()
