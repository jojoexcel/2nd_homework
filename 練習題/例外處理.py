try:
    num= int(input('輸入整數：'))
except ValueError as err1:
    print(f'請輸入阿拉伯數字 ({err1})')
except TypeError as err2:
    print(f'請輸入整數 ({err2})')
except KeyboardInterrupt:
    print('使用者中斷程式')
except Exception as e:
   print(f'錯誤訊息：{e}')
else:
    print(f"{num} 為 {'奇數' if num% 2 else '偶數'}")
finally:
    print('再見')