# 统一运行入口

from password_validator import validate_password
from phone_validator import is_valid_phone
from shopping_cart import calculate_total


def run_demo():
    """运行手机号、密码和购物车三个业务场景。"""
    phone = "13812345678"
    password = "Abc12345!"
    cart = [
        {"name": "鼠标", "price": 99.0, "quantity": 2},
        {"name": "键盘", "price": 199.0, "quantity": 1},
    ]

    print("一、手机号校验")
    print(f"手机号：{phone}")
    print(f"校验结果：{'通过' if is_valid_phone(phone) else '不通过'}")

    print("\n二、密码校验")
    password_result = validate_password(password)
    print(f"校验结果：{'通过' if password_result['valid'] else '不通过'}")
    if password_result["errors"]:
        print("问题：", "；".join(password_result["errors"]))

    print("\n三、购物车总价")
    try:
        total = calculate_total(cart)
        print(f"购物车总价：{total:.2f} 元")
    except ValueError as error:
        print(f"购物车数据有误：{error}")


if __name__ == "__main__":
    run_demo()
