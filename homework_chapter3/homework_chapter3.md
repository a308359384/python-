暨南大学本科实验报告专用纸
课程名称             python程序设计            成绩评定                     
实验项目名称                   python作业第三章                               
姓名 崔嘉容 学号 2020100069 学院 网络空间安全 专业 网络空间安全 
实验时间 2023 年 10 月 9 日 ～  10 月 16 日  实验地点：    516    
一、实验目的
掌握三种基本控制结构：顺序结构、选择结构、循环结构。
二、实验环境和设备
实验环境：操作系统-Windows10，python版本-3.11.3，开发环境-pycharm
实验设备：华为MateBook14-2020，处理器-i7-10510U，内存-16GB
三、 实验内容和结果
题目一：编写程序，使用不同的实现方法，输出2000~4000之间的所有闰年，每行显示10个数字。
实验代码：
方法一：使用循环和条件语句
def find_leap_years(start, end):
    leap_years = []
    for year in range(start, end+1):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            leap_years.append(year)
    return leap_years

start_year = 2000
end_year = 4000
leap_years = find_leap_years(start_year, end_year)

for i, year in enumerate(leap_years):
    print(year, end=' ')
    if (i + 1) % 10 == 0:
        print()


方法二：使用列表推导式
start_year = 2000
end_year = 4000

leap_years = [year for year in range(start_year, end_year+1) if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]

for i, year in enumerate(leap_years):
    print(year, end=' ')
    if (i + 1) % 10 == 0:
        print()


方法三：使用datetime模块
import datetime

def find_leap_years(start, end):
    leap_years = []
    for year in range(start, end+1):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if datetime.date(year, 2, 29).year == year:
                leap_years.append(year)
    return leap_years

start_year = 2000
end_year = 4000
leap_years = find_leap_years(start_year, end_year)

for i, year in enumerate(leap_years):
    print(year, end=' ')
    if (i + 1) % 10 == 0:
        print()

实验结果：
 

 
 实验分析和总结：
这个实验的目的是编写一个程序来输出2000到4000年之间的所有闰年，并且每行显示10个数字。使用三种不同的实现方法，分别使用了循环和条件语句、列表推导式以及`datetime`模块。
1. 使用循环和条件语句
这是最基本的实现方法，通过一个循环遍历2000到4000年的所有年份，然后使用条件语句来判断是否为闰年。如果是闰年则将其添加到一个列表中，最后按照要求进行输出。
2. 使用列表推导式
这种方法是一种更为简洁的实现方式，利用了Python中的列表推导式来过滤出满足条件的年份。这种方式相对于第一种方法更为紧凑。
3. 使用`datetime`模块
这种方法利用了Python的`datetime`模块，它提供了日期处理的功能。通过尝试创建2月29日的日期对象来检查是否是闰年，从而确定是否将其添加到闰年列表中。 
题目二: 编写程序，计算Sn=1-3+5-7+9-11+…  。
实验代码：
def calculate_Sn(n):
    Sn = 0
    for i in range(1, n+1):
        if i % 2 == 1:
            Sn += 2*i - 1
        else:
            Sn -= 2*i - 1
    return Sn

n = int(input("请输入要计算的项数："))
result = calculate_Sn(n)
print(f"S{n} = {result}")
实验结果：
 
 
实验分析和总结：
通过定义一个函数 calculate_Sn(n) 来计算前 n 项的和，其中 n 为用户输入的项数。在 calculate_Sn 函数中，使用循环来遍历每一项，根据奇偶性来决定是加上还是减去该项。最终计算得到和，并输出结果。
在使用 input 函数来接收用户的输入，并将其转换为整数类型。如果用户输入的不是一个合法的整数，可能会引发异常，需要进行相应的错误处理。
直接使用input会出现“TypeError: can only concatenate str (not "int") to str”的报错，需要使用强制类型转换将输入的字符串转为int类型的值。
 
题目三：编写程序，打印九九乘法表。要求输出的九九乘法表的各种显示效果（上三角、下三角、矩形块等方式）。
实验代码：
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

实验结果：
 
 
实验分析和总结：
打印上三角、下三角和矩阵块形式的九九乘法表的思路：
1. 上三角形的九九乘法表：只需要输出乘法表的上半部分（即 i>=j 的部分）。使用两层循环，外层循环 i 控制行数，内层循环 j 控制列数。在内层循环中，只打印满足 j<=i 的部分。
2. 下三角形的九九乘法表：只需要输出乘法表的下半部分（即 i<=j 的部分）。同样使用两层循环，外层循环 i 控制行数，内层循环 j 控制列数。在内层循环中，我们打印满足 i<=j 的部分。
3. 矩阵块形式的九九乘法表：包括所有乘积，使用两层循环遍历所有行和列。
格式控制和对齐：
问题：打印乘法表时，会出现格式不对齐的情况，导致表格显示混乱。
解决方法：在打印每个乘积时，可以使用制表符 \t 或者手动添加空格来保持格式的整齐。可以根据实际情况进行调整
 
题目四: 编写程序，产生两个0~100之间（包括0和100）的随机整数a和b。求这两个整数的最大公约数和最小公倍数。
实验代码：
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

实验结果：
 
 
实验分析和总结：
编写这个程序需要分为以下几个步骤：
生成随机整数a和b：使用Python的random模块中的randint()函数生成两个0~100之间的随机整数，分别赋值给变量a和b。
求最大公约数：编写一个函数gcd(x, y)，实现辗转相除法来求解最大公约数。辗转相除法是一种有效的求解最大公约数的算法，它通过反复地用除数去除余数来求解。
求最小公倍数：编写一个函数lcm(x, y)，利用最大公约数来求得最小公倍数。最小公倍数可以通过两数相乘除以最大公约数来得到。
如何使用Python生成指定范围内的随机整数？使用random.randint(a, b)函数可以生成指定范围内的随机整数，其中a和b分别是随机数的最小值和最大值。
如何使用辗转相除法求解两个数的最大公约数？辗转相除法是一种常用的求解最大公约数的算法，通过反复地用除数去除余数来求解，直到余数为0。这样得到的除数就是最大公约数。
如何通过最大公约数求得两个数的最小公倍数？最小公倍数可以通过两数的乘积除以最大公约数来得到。
如何使用格式化字符串输出结果？使用f-string或者其他格式化字符串的方法可以清晰地输出结果。
