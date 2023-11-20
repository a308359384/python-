import math
def solve_quadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root
    else:
        return None
# 给定方程的系数
a = 1
b = 10
c = 16
# 求解方程
solutions = solve_quadratic_equation(a, b, c)
# 输出结果
if solutions is not None:
    if len(solutions) == 2:
        print(f"方程的两个实根分别为: x1 = {solutions[0]}, x2 = {solutions[1]}")
    else:
        print(f"方程有一个实根: x = {solutions[0]}")
else:
    print("方程无实根")
