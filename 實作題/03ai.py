def sum_allvalue(all_value):
    sumdate = 0
    for value_x in all_value:
        sumdate += value_x
    return sumdate


student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}  # 原始字典

# 初始化總和變數
all_value = student_scores.values()
sumdate = sum_allvalue(all_value)

# 輸出總和

print("總和：", sumdate)
