import os
import time  # 導入 time 模組
from datetime import datetime, timedelta

os.system('cls')


def time_decorator(func):
    """裝飾器"""

    def wrapper():
        """在執行 func() 前後顯示時間"""
        now = datetime.now()  # 獲取當前時間
        formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")  # 格式化為 "yyyy-mm-dd hh:mm:SS"
        print(f"現在時間：{formatted_now}")
        time.sleep(0.1)  # 停止一秒
        func()

        end_time = datetime.now()  # 獲取執行結束時間
        formatted_end_time = end_time.strftime("%Y-%m-%d %H:%M:%S")  # 格式化為 "yyyy-mm-dd hh:mm:SS"
        execution_time_seconds = end_time - now  # 取得 timedelta 的秒數部分

        print(f"執行結束時間：{formatted_end_time}")
        print(f"執行時間：{execution_time_seconds}")

    return wrapper


@time_decorator
def greet():
    """被裝飾的函式"""
    print("哈囉！歡迎來到 Python 裝飾器的世界！")


greet()
