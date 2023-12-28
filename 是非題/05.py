# 定義一個 NoneType 物件
none_obj = None

# 嘗試改變它的值
try:
    none_obj += 1
except TypeError as e:
    print(f"錯誤: {e}")
