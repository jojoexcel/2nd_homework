import os

# 在 Windows 中清屏
os.system('cls')


def reverse_string(input_str):
    # 使用 list() 和 reverse() 方法反轉字串
    # return ''.join(list(input_str)[::-1])
    return input_str[::-1]


# 測試
original_str = "Hello, World!"
reversed_str = reverse_string(original_str)
print(f"原始字串: {original_str}, 反轉後: {reversed_str}")
