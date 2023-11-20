import tkinter as tk
from tkinter import messagebox

def filter_values():
    min_value = entry_min.get()
    max_value = entry_max.get()

    try:
        min_value = int(min_value)
        max_value = int(max_value)
        if min_value > max_value:
            messagebox.showwarning("警告", "下限不能大于上限")
            return
    except ValueError:
        messagebox.showerror("错误", "请输入有效的整数")
        return

    result_text.configure(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)

    values = input_entry.get().split()

    for value in values:
        try:
            value = int(value)
            if min_value <= value <= max_value:
                result_text.insert(tk.END, str(value) + '\n')
        except ValueError:
            pass

    result_text.configure(state=tk.DISABLED)

# 创建主窗口
root = tk.Tk()
root.title("过滤器")
root.geometry("400x300")  # 设置窗口大小

# 创建用户输入部分
label_min = tk.Label(root, text="下限:")
entry_min = tk.Entry(root)
label_max = tk.Label(root, text="上限:")
entry_max = tk.Entry(root)
input_entry = tk.Entry(root, width=30)

# 提示用户输入多个值
label_input = tk.Label(root, text="请输入多个值（以空格分隔）:")

# 创建“过滤”按钮
filter_button = tk.Button(root, text="过滤", command=filter_values)

# 创建输出部分
result_text = tk.Text(root, height=10, width=30, state=tk.DISABLED)

# 布局界面元素
label_min.grid(row=0, column=0, padx=5, pady=5)
entry_min.grid(row=0, column=1, padx=5, pady=5)
label_max.grid(row=0, column=2, padx=5, pady=5)
entry_max.grid(row=0, column=3, padx=5, pady=5)
label_input.grid(row=1, column=0, columnspan=4, padx=5, pady=5)
input_entry.grid(row=2, column=0, columnspan=4, padx=5, pady=5)
filter_button.grid(row=3, column=0, columnspan=4, padx=5, pady=5)
result_text.grid(row=4, column=0, columnspan=4, padx=5, pady=5)

# 运行主事件循环
root.mainloop()
