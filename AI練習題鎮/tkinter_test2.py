import tkinter as tk


def on_button_click():
    label.config(text="你好")


form = tk.Tk()  # 呼叫 tk.TK() 建立視窗
form.title("Tkinter Grid 佈局範例")

form.geometry("400x300")  # 設定視窗寬高

frame1 = tk.Frame(form, bg='red', width=50, height=50)
frame2 = tk.Frame(form, bg='yellow', width=50, height=50)
frame3 = tk.Frame(form, bg='blue', width=50, height=50)
frame4 = tk.Frame(form, bg='lightgreen', width=50, height=50)
frame5 = tk.Frame(form, bg='lightblue', width=50, height=50)


frame1.grid(row=0, column=1)
frame2.grid(row=1, column=1)
frame3.grid(row=2, column=1)
frame4.grid(row=0, column=0)
frame5.grid(row=0, column=2)

# 設定 column 1, 2, 3 的權重為 1，亦即平均分配中間的剩餘空間，各自擁有 33.3%
# form.columnconfigure((1, 2, 3), weight=1)
frame5.rowconfigure(0, weight=1)
frame4.rowconfigure(0, weight=1)
# form.rowconfigure((0, 2), weight=1)
# form.rowconfigure(0, weight=1)
# form.columnconfigure(1, weight=1)

form.mainloop()  # 等待處理事件保持視窗運行
