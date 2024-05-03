# 1. 請合併以下兩個字串，再將字串進行反轉
# "Hello" 和 "World"
x = "Hello"
y = "World"
p = x + y
a = list(p)
a.reverse()
a = ''.join(a)
print(a)
