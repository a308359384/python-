import sys
def my_print(*args, sep=' ', end='\n', file=None):
    output = sep.join(map(str, args)) + end
    if file is not None:
        with open(file, 'a') as f:
            f.write(output)
    else:
        sys.stdout.write(output)
        sys.stdout.flush()

# 示例用法
my_print("Hello", "World")  # 输出: Hello World

my_print(1, 2, 3, sep='. ')  # 输出: 1. 2. 3

my_print("Custom", "Print", end=' ')  # 输出: Custom Print

my_print("Save to file", file='output.txt')  # 将输出保存到 output.txt 文件中

