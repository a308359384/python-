def compound_interest(principal, rate, years):
    if principal < 0 or rate < 0 or years < 0:
        raise ValueError("输入不能为负数")
    amount = principal * (1 + rate)**years
    return round(amount, 1)

try:
    principal = float(input("请输入本金（数字）："))
    rate = float(input("请输入年利率（小于1的小数）："))
    if not (0 < rate < 1):
        raise ValueError("利率必须在0到1之间")
    years = int(input("请输入存款年份（整数）："))

    result = compound_interest(principal, rate, years)

    print(f"在{years}年后，您的本金将会增长到{result}。")
except ValueError as e:
    print(f"发生错误：{e}")
except Exception as e:
    print(f"发生未知错误：{e}")


