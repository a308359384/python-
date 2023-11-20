import datetime

def calculate_age(birth_year, birth_month):
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month

    age_years = current_year - birth_year
    age_months = current_month - birth_month

    if age_months < 0:
        age_years -= 1
        age_months += 12

    return age_years, age_months

# 获取用户输入姓名
name = input("请输入您的姓名：")

# 获取用户输入出生年份和月份，并添加合法性检查
while True:
    try:
        birth_year = int(input("请输入您的出生年份："))
        birth_month = int(input("请输入您的出生月份："))
        current_year = datetime.datetime.now().year

        if birth_year > current_year or birth_year < 0:
            raise ValueError("出生年份无效，请重新输入。")

        if birth_month > 12 or birth_month < 1:
            raise ValueError("出生月份无效，请重新输入。")

        if birth_year == current_year and birth_month > datetime.datetime.now().month:
            raise ValueError("出生月份无效，请重新输入。")

        if current_year - birth_year > 120:  # 设置一个合理的年龄范围（例如，120岁）
            confirm = input("您输入的年龄超出正常范围，是否确认？(输入 'yes' 确认，其他输入将重新输入)")
            if confirm.lower() != 'yes':
                continue

        break  # 输入合法，退出循环
    except ValueError as e:
        print(e)

# 计算年龄
age_years, age_months = calculate_age(birth_year, birth_month)
# 输出姓名和年龄
if age_years == 0:
    print(f"{name}先生/女士，您今年{age_months}个月大。")
else:
    print(f"{name}先生/女士，您今年{age_years}岁了。")
