import getpass

username = input("请输入用户名: ")
passwd = getpass.getpass("请输入密码: ")

if username == 'admin' and passwd == '123456':
    print("登录成功")
else:
    print("登录失败")
