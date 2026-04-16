import time as t
import random
"""
循环结构
For-in和While的简单使用

version:1.0
Author:x鑫
"""

'''
测试的代码
import time

while 1:
    print('hello,world')
    time.sleep(1)

'''

'''
# 使用for-in每一秒输出一次“hello，world”,持续1小时
for _ in range(10):
    print("hello，world")
    t.sleep(1)
'''

"""
range(101)：可以用来产生0到100范围的整数，需要注意的是取不到101。
range(1, 101)：可以用来产生1到100范围的整数，相当于是左闭右开的设定，即[1, 101)。
range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长（跨度），即每次递增的值，101取不到。
range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长（跨度），即每次递减的值，0取不到。
"""

# 用for-in实现从1到100的整数求和
total = 0
for i in range(1, 101):
    total += i
print("1-100总和：", total)

# 1-100 偶数和
total_even = 0
for i in range(1, 101):
    if i % 2 == 0:
        total_even += i
print(total_even)
# 用内置函数求100内的偶数
print(sum(range(2, 101, 2)))

# 用While实现1-100 偶数求和
total = 0
i = 2
while True:
    total += i
    i += 2
    if i > 100:
        break
print(total)

# 分割线
print("--------------------------------------------------------------------------")

# 输出乘法口诀表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}x{j}={i * j}', end='\t')
    print()
# 分割线
print("--------------------------------------------------------------------------")

'''
# 判断素数
# 要求输入1个大于1的正整数，判断其是否未素数
# 素数指的是只能被 1 和自身整除的大于 1 的整数
num = int(input("请输入一个正整数："))
end = int(num ** 0.5)
isNo = True  # 是否是素数
for i in range(2, end+1):  # 在 2 到num**0.5的范围找因子，如果找到num的因子，就一定不是素数
    if num % i == 0:
        isNo = False
        break
if isNo:
    print(f'{num}是素数')
else:
    print(f'{num}不是素数')
# 分割线
print("--------------------------------------------------------------------------")
'''

'''
# 最大公约数
# 要求：输入两个大于 0 的正整数，求两个数的最大公约数。
# 两个数的最大公约数是两个数的公共因子中最大的那个数。
x = int(input("x = "))
y = int(input("y = "))
while y % x != 0:
    x, y = y % x, x  # 将 y%x 给 x,x给y
print(f'最大公约数：{x}')

'''

# 猜数字游戏
# 要求：计算机出一个 1 到 100 之间的随机数，玩家输入自己猜的数字，
#      计算机给出对应的提示信息“大一点”、“小一点”或“猜对了”，
#      如果玩家猜中了数字，计算机提示用户一共猜了多少次，游戏结束，否则游戏继续。
answer = random.randrange(1, 101)
count = 0
while True:
    count += 1
    num = int(input("请输入："))
    if num < answer:
        print('大一点.')
    elif num > answer:
        print('小一点.')
    else:
        print("猜对了")
        break
print(f"你一共猜了{count}次")

"""
for-in和while的使用区别：
前者适用已知循环次数
后者适用未知循环次数
可以用break结束当前循环结构
也可以用continue跳出本次循环进入下次循环
"""
