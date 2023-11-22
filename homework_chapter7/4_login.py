import getpass


def read_user_list(filename):
    user_list = {}
    with open(filename, 'r') as file:
        for line in file:
            username, password = line.strip().split(',')
            user_list[username] = password
    return user_list


def write_log(log_message):
    with open('warnlog.txt', 'a') as file:
        file.write(log_message + '\n')


def login(username, password):
    user_list = read_user_list('user_list.txt')
    if username not in user_list:
        log_message = f"[error] {username} is not exist - {time.strftime('%Y-%m-%d %H:%M:%S')}"
        write_log(log_message)
        raise Exception(f"User '{username}' does not exist.")

    if user_list[username] == password:
        print(f"Welcome, {username}!")
    else:
        password_wrong = False  # 添加一个布尔变量来标记密码是否输入错误
        for _ in range(3):
            password_attempt = getpass.getpass("请输入密码：")
            if user_list[username] == password_attempt:
                print(f"Welcome, {username}!")
                return
            else:
                password_wrong = True

        if password_wrong:
            log_message = f"[warning] {username}-Password error three times - {time.strftime('%Y-%m-%d %H:%M:%S')}"
            write_log(log_message)
            print(f"User '{username}' locked due to three incorrect password attempts.")
            return


import time

try:
    username = input("请输入用户名：")
    password = getpass.getpass("请输入密码：")
    login(username, password)
except Exception as e:
    print(e)
