import os

# 在 Windows 中清屏
os.system('cls')


def print_star(n):
    spaces_list = []  # 用來存儲每一行的 spaces
    for i in range(n):  # i會從0開始
        spaces = abs(n // 2 - i)  # 計算前置空白
        stars = n - 2 * spaces  # 星數從1至N setp 2
        print(" " * spaces + "*" * stars)
        spaces_list.append({"列": i + 1, "空白": spaces, "星星": stars})

    # 列印 spaces_list
    print("Spaces List:", spaces_list)


while True:
    x_str = input(r"請輸入最多的星星數：(限奇數) ")
    try:
        n = int(x_str)
        if n % 2 != 0:
            print_star(n)
            break  # 如果條件滿足，跳出循環
        else:
            print("輸入不合法，請確保輸入是奇數。")
    except ValueError:
        print("請輸入有效的數字。")
