import tkinter as tk


def on_button_click():
    kk = label.cget("text")
    if kk == '你好':
        label.config(text="點我")
    else:
        label.config(text="你好")


form = tk.Tk()  # 呼叫 tk.Tk() 建立視窗
form.title("Tkinter Pack 佈局範例")
form.geometry("400x300")  # 設定視窗寬高

# 添加 label 和 button 元件
label = tk.Label(form, text="Hello, Pack!", bg="green", fg="#263238", font=("Arial", 24))
label.pack(side="top", fill="both", expand=True, padx=10, pady=5)

button = tk.Button(form, text="點我", command=on_button_click)
button.pack(side="left", anchor="nw", padx=10, pady=10)

form.mainloop()  # 等待處理事件保持視窗運行
