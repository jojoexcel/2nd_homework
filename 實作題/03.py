# 3. 請加總與平均(至小數2位)以下字典內的分數，再將結果放入相同的字典內，並新增 total 與 avg 二個 Key-Value pairs
''' AI優化
def sum_all_value(all_value):
    return sum(all_value)

def avg_value(sum_value, count):
    return sum_value / count

student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}  # 原始字典

# 取得所有值
all_values = student_scores.values()

# 計算總和
total_score = sum_all_value(all_values)

# 計算平均值
average_score = avg_value(total_score, len(student_scores))

# 輸出總和與平均值
print("總和：", total_score)
print("平均：", round(average_score, 2))
'''


def sum_allvalue(all_value):
    sumdate = 0
    for value_x in all_value:
        sumdate += value_x
    return sumdate


def avg_value(all_nu, sumdate):
    avg = sumdate / all_nu
    return avg


student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}  # 原始字典
# 初始化總和變數
all_value = student_scores.values()
sumdate = sum_allvalue(all_value)
all_nu = len(student_scores)
avg = avg_value(all_nu, sumdate)

# 輸出總和
print("總和：", sumdate)
print("平均：", avg)
student_scores['total'] = sumdate
student_scores['avg'] = round(avg, 2)
print(student_scores)
