# 自數字 1-15 亂數取出 8 個不重複的整數
# 設定起啟
# 設定取出數
# 判別設定
# 輸出結果
import random


def random_unique_numbers(start, end, count):
    # 檢查輸入是否有效
    if not isinstance(start, int) or not isinstance(end, int) or not isinstance(count, int):
        raise ValueError("起始值、終止值和取出數必須是整數")
    if start >= end:
        raise ValueError("起始值必須小於終止值")
    if count > (end - start + 1):
        raise ValueError("取出數大於可用的數字範圍")

    result = set()
    while len(result) < count:
        result.add(random.randint(start, end))

    return list(result)


# 設定起始值和終止值
start = 1
end = 100
# 設定取出數
count = 3

try:
    # 獲取結果
    result = random_unique_numbers(start, end, count)
    # 輸出結果
    print("隨機取出的不重複整數：", result)
except ValueError as e:
    print("錯誤：", e)
