import tkinter as tk

from 亂數LIST import random_unique_numbers


def generate_random_numbers():
    try:
        start = int(entry_start.get())
        end = int(entry_end.get())
        count = int(entry_count.get())

        result = random_unique_numbers(start, end, count)
        label_result.config(text="隨機取出的不重複整數：" + str(result))
    except ValueError as e:
        label_result.config(text="錯誤：" + str(e))


# 建立主視窗
root = tk.Tk()
root.title("隨機數字生成器")

# 起始值輸入
label_start = tk.Label(root, text="起始值：")
label_start.grid(row=0, column=0)
entry_start = tk.Entry(root)
entry_start.grid(row=0, column=1)

# 終止值輸入
label_end = tk.Label(root, text="終止值：")
label_end.grid(row=1, column=0)
entry_end = tk.Entry(root)
entry_end.grid(row=1, column=1)

# 取出數輸入
label_count = tk.Label(root, text="取出數：")
label_count.grid(row=2, column=0)
entry_count = tk.Entry(root)
entry_count.grid(row=2, column=1)

# 生成按鈕
button_generate = tk.Button(root, text="生成", command=generate_random_numbers)
button_generate.grid(row=3, column=0, columnspan=2)

# 顯示結果
label_result = tk.Label(root, text="")
label_result.grid(row=4, column=0, columnspan=2)

# 運行主迴圈
root.mainloop()
