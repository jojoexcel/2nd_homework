def divide(a, b):
    if b == 0:
        raise ValueError("不能除以0")
    return a / b


print(divide(5,0))