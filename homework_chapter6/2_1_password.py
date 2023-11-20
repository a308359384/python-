import tkinter as tk
from tkinter import messagebox
import getpass

def check_login(event=None):
    username = entry_username.get()
    passwd = entry_password.get()

    if (username, passwd) in user_credentials:
        messagebox.showinfo("登录结果", "登录成功")
        # 登录成功后清空密码输入框
        entry_password.delete(0, tk.END)
    else:
        messagebox.showerror("登录结果", "登录失败")

# 创建主窗口
root = tk.Tk()
root.title("登录窗口")
root.geometry("300x200")

# 用户名和密码的列表
user_credentials = [
    ('admin', '123456'),
    ('user1', 'password1'),
    ('user2', 'password2')
]

# 创建用户名和密码的Label和Entry
label_username = tk.Label(root, text="用户名:")
entry_username = tk.Entry(root)

label_password = tk.Label(root, text="密码:")
entry_password = tk.Entry(root, show="*")  # 使用show参数将密码输入变成掩码

# 在密码输入框上绑定回车键事件
entry_password.bind('<Return>', check_login)

# 创建登录按钮
login_button = tk.Button(root, text="登录", command=check_login)

# 布局界面元素
label_username.pack(pady=(10, 0))
entry_username.pack(pady=(0, 10))
label_password.pack(pady=(10, 0))
entry_password.pack(pady=(0, 10))
login_button.pack()

# 运行主事件循环
root.mainloop()
