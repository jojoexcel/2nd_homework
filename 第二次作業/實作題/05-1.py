# 讓使用者輸入最長的一列星星數(奇數)，然後動態產生以下的星星圖案。
# 如果是偶數自動+1
import os

# 在 Windows 中清屏
os.system('cls')


def print_start(n):
    for i in range(n):
        spaces = abs(n // 2 - i)  # 計算前置空白
        # print(spaces)
        stars = n - 2 * spaces  # 星數從1至N setp 2
        print(" " * spaces + "*" * stars)


while True:
    x_str = input(r"請輸入最多的星星數：(限奇數) ")
    try:
        n = int(x_str)
        if n % 2 != 0:
            print_start(n)
            break  # 如果條件滿足，跳出循環
        else:
            n += 1  # n=n+1      js用 n++
            print_start(n)
            break  # 如果條件滿足，跳出循環
            # print("輸入不合法，請確保輸入是3到100之間的奇數。")
    except ValueError:
        print("請輸入有效的數字。")
