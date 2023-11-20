import math
def calculate_sphere_properties(radius):
    if radius < 0:
        raise ValueError("半径不能为负数")
    surface_area = round(4 * math.pi * radius ** 2, 1)
    volume = round((4 / 3) * math.pi * radius ** 3, 1)
    return surface_area, volume
try:
    radius = float(input("请输入球的半径（数字）："))
    surface_area, volume = calculate_sphere_properties(radius)

    print(f"球的表面积为：{surface_area} ")
    print(f"球的体积为：{volume} ")
except ValueError as e:
    print(f"发生错误：{e}")
except Exception as e:
    print(f"发生未知错误：{e}")
