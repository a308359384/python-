import sys

# 获取命令行参数中的n值
n = int(sys.argv[1])

# 保存原始的标准输出流
original_stdout = sys.stdout

# 打开一个文件作为新的标准输出流
with open('out.log', 'w') as f:
    sys.stdout = f

    # 输出需要重定向的内容
    values = list(range(n + 1))
    values_times_2 = [2 * i for i in values]
    powers_of_2 = [2 ** i for i in values]

    print(values)
    print(values_times_2)
    print(powers_of_2)

# 恢复原始的标准输出流
sys.stdout = original_stdout
