import os

# 在 Windows 中清屏
os.system('cls')


def is_prime_number(n):
    if n == 2 or n == 3:
        return True
    elif n > 4:
        m = n % 6

        if m != 1 and m != 5:
            return False

        for i in range(5, int(n**0.5) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False

        return True
    else:
        return False


# 測試
while True:
    number = input(r"請輸入任意數值,enter 離開 ")
    if not number:
        break
    number = int(number)
    print(f"{number} 是否為質數: {is_prime_number(number)}")
