def calculate_average(records):
    total = sum(record['grade'] for record in records)
    average = total / len(records)
    return total, round(average, 2)


# 初始化空列表用於存放記錄
records_list = []

# 連續輸入姓名與成績，直到按下 Enter 離開
while True:
    name = input("請輸入姓名（按下 Enter 結束）：")
    if not name:
        break

    while True:
        grade_input = input("請輸入成績（按下 Enter 回上一層不存這筆）：")
        if not grade_input:  # 如果使用者直接按下 Enter 結束，跳出內層迴圈
            break

        try:
            grade = float(grade_input)
            if 0 <= grade <= 100:
                # 將姓名與成績以字典形式加入列表
                records_list.append({'name': name, 'grade': grade})
                break  # 成績符合要求，跳出內層迴圈
            else:
                print("請輸入有效的成績（介於 0 到 100 之間的數字）。")
        except ValueError:
            print("請輸入有效的數字。")

# 顯示所有記錄
print("\n所有記錄：")
for record in records_list:
    print(record)

# 計算總分與平均值
total_score, average_score = calculate_average(records_list)

# 顯示總分與平均值
print("\n總分：", total_score)
print("平均：", average_score)
