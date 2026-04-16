import random
"""
list列表的简单使用
Version:1.0
Author:x鑫
"""

# 创建和运算
item1 = list(range(1, 10))
item2 = list('hello')
print(item1)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(item2)  # ['h', 'e', 'l', 'l', 'o']
print("----------------------------------------------------")
# 可用+号将俩个列表拼接
print(item1 + item2)
# 可用*号实现列表重复运算
print(item1 * 5)
# 可用 in 和 not in 判断一个元素在不在列表里面
print(3 in item1)  # True
print('h' in item1)  # False
print('l' not in item2)  # False
print(4 not in item2)  # True
print("----------------------------------------------------")
# 要一次性访问多个元素，可以用切片运算
# [开始位置:结束位置（不访问）:跨度]
item3 = ['apple', 'strawberry', 'durian', 'peach', 'watermelon']
print(item3[0:3:1])
print(item3[1:3:1])
print(item3[0:5:2])
print(item3[-4:-1:1])
print(item3[-2:-6:-1])
print("----------------------------------------------------")
# 如果开始位置为0，切片时候可以省略
# 如果结束位置为列表的长度，切片时也可以省略
# 如果跨度等于1时，切片也可以省略
print(item3[0:3])
print(item3[1:3])
print(item3[::2])
print(item3[-4:-1])
print(item3[-2::-1])
print("----------------------------------------------------")
# 切片也可以修改值
item3[1:3] = ['xx', 'oo']
print(item3)
print("----------------------------------------------------")
# 逐个拿到列表元素
# 一、通过索引拿元素
languages = ['python', "Java", "C++", "Kotlin"]
for index in range(len(languages)):
    print(languages[index])
print("----------------------------------------------------")
# 二、直接用列表循环，循环变量就是列表元素的代表
for language in languages:
    print(language)
print("----------------------------------------------------")
# 将一颗色子掷6000次，统计每种点数出现的次数

counts = [0] * 6
for _ in range(6000):
    s = random.randrange(1, 7)
    counts[s-1] += 1
for count in counts:
    print(count)
