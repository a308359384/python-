def print_upper_triangle():
    print("\n上三角形的九九乘法表：")
    for i in range(1, 10):
        for j in range(i, 10):
            print(f'{j}x{i}={i*j}', end='\t')
        print()

def print_lower_triangle():
    print("\n下三角形的九九乘法表：")
    for i in range(1, 10):
        for j in range(1, i+1):
            print(f'{j}x{i}={i*j}', end='\t')
        print()

def print_rectangle():
    print("\n矩形块的九九乘法表：")
    for i in range(1, 10):
        for j in range(1, 10):
            print(f'{j}x{i}={i*j}', end='\t')
        print()

# 调用各种打印函数
print_upper_triangle()
print_lower_triangle()
print_rectangle()
