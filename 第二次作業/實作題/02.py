# 請寫一隻可接受使用者不斷輸入英文姓名的程式，直到按下Enter 後結束，輸入的姓名請放入 List 中，結束後請輸出：
# a. 依字母遞增排序與遞減排序
# b. 依字數多寡遞增與遞減排序
import re


def is_english_name(name):
    # 此正規表示式確保名字只包含英文字母 可以空白
    pattern = re.compile(r'^[a-zA-Z ]+$')
    return bool(pattern.match(name))


def get_names():
    names = []
    while True:
        name = input("請輸入英文姓名（按下 Enter 結束）：")
        if not name:
            break
        # 驗證是否為英文姓名
        if is_english_name(name):
            names.append(name)
        else:
            print("請輸入有效的英文姓名。")
    return names


def print_sorted_names(names, key=None, reverse=False):
    sorted_names = sorted(names, key=key, reverse=reverse)
    print(sorted_names)


# 取得姓名列表
names_list = get_names()

# 依字母遞增排序與遞減排序
print("按字母遞增排序：", end=" ")
print_sorted_names(names_list)

print("按字母遞減排序：", end=" ")
print_sorted_names(names_list, reverse=True)

# 依字數多寡遞增排序與遞減排序
print("按字數遞增排序：", end=" ")
print_sorted_names(names_list, key=len)

print("按字數遞減排序：", end=" ")
print_sorted_names(names_list, key=len, reverse=True)
