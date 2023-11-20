name = str(input("请输入姓名："))
# 获取用户输入出生年份，并添加合法性检查
while True:
    try:
        birth_year = int(input("请输入您的出生年份："))
        if birth_year > 2023:  # 出生年份不能超过当前年份
            raise ValueError("出生年份不能超过当前年份！")
        if birth_year < 0:
            raise ValueError("出生年份不能为负数！")
        break  # 输入合法，退出循环
    except ValueError as e:
        print(f"输入非法：{e}")
age = 2023 - birth_year
print(name + "今年" + str(age) + "岁")
