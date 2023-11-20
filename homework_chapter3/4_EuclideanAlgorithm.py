import random

# 生成随机整数 a 和 b
a = random.randint(0, 100)
b = random.randint(0, 100)

# 辗转相除法求最大公约数
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# 最小公倍数通过最大公约数求得
def lcm(x, y):
    return x * y // gcd(x, y)

# 输出随机生成的两个整数
print(f"随机生成的整数 a = {a}, b = {b}")

# 计算最大公约数和最小公倍数
gcd_result = gcd(a, b)
lcm_result = lcm(a, b)

print(f"最大公约数为: {gcd_result}")
print(f"最小公倍数为: {lcm_result}")
