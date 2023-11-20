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
