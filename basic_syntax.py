# 基础语法练习

def greet_user(name):
    """返回一条欢迎信息。"""
    return f"你好，{name}！欢迎开始学习 Python。"


def get_adult_message(age):
    """根据年龄返回是否成年的提示。"""
    if age >= 18:
        return "已满 18 岁"
    return "未满 18 岁"


def calculate_score_average(scores):
    """计算分数列表的平均值；空列表返回 0。"""
    if not scores:
        return 0
    return sum(scores) / len(scores)


def print_student_info(student):
    """打印字典中的学生信息。"""
    print(f"姓名：{student['name']}")
    print(f"年龄：{student['age']}")
    print(f"学习方向：{student['direction']}")


def main():
    # 1. 变量、字符串、数字和布尔值
    name = "测试学习者"
    age = 25
    is_learning = True
    print("姓名：", name)
    print("年龄：", age)
    print("是否正在学习：", is_learning)
    print(greet_user(name))
    print()

    # 2. 列表：保存多个有顺序的数据
    skills = ["Python", "手工测试", "Git"]
    skills.append("pytest")
    skills[0] = "Python 基础"
    print("技能列表：")
    for skill in skills:
        print("-", skill)
    print()

    # 3. 字典：用键和值描述一个对象
    student = {
        "name": name,
        "age": age,
        "direction": "软件测试",
    }
    print_student_info(student)
    print()

    # 4. if：根据条件执行不同逻辑
    print(get_adult_message(age))
    print()

    # 5. for：遍历列表并完成重复计算
    scores = [80, 90, 85]
    total = 0
    for score in scores:
        total += score
    print("总分：", total)
    print("平均分：", calculate_score_average(scores))


if __name__ == "__main__":
    main()
