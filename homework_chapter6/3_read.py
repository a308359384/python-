import sys
import chardet

# 获取命令行参数中的文件名
file_name = sys.argv[1]

# 检测文件编码
with open(file_name, 'rb') as f:
    rawdata = f.read()
    result = chardet.detect(rawdata)
    encoding = result['encoding']

# 打开文件
with open(file_name, 'r', encoding='utf-8') as file:
    # 逐行读取并输出
    for i, line in enumerate(file, 1):
        print(f'Line {i}: {line}', end='')


# python 3_read.py file1.txt
