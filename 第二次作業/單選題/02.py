class MyClass:
    class_variable = 30

    def __init__(self):
        self.instance_variable = 40


obj1 = MyClass()
print(obj1.class_variable)  # 可以訪問類別變數
print(obj1.instance_variable)  # 可以訪問實例變數
