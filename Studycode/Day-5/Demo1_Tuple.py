"""
元组的简单使用
Version:1.0
Author:x鑫
"""

# 元组是不可变类型
# 定义了就不能对元素进行添删改,否则就会报错

# 定义一个三元组
t1 = (11,22,48)
# 定义一个四元组
t2 = ('某人', 55, True, "某地")

# 查看类型
print(type(t1))  # <class 'tuple'>
print(type(t2))  # <class 'tuple'>

# 查看数量
print(len(t1))  # 3
print(len(t2))  # 4

# 切片运算
print(t2[:3])  # ('某人', 55, True)
print(t2[::3])  # ('某人', '某地')

# 索引运算
print(t1[0])  # 11
print(t1[2])  # 48
print(t2[-1])  # 某地

# 遍历元组的元素
for item in t2:
    print(f"{item}", end=" ")

# 成员运算
print(11 in t1)  # True
print(44 in t1)  # False
print('某人' in t2)  # True

# 拼接
t3 = t1+t2
print(t3)

# 一个元组中只有一个元素时，括号里面需要加逗号，否则就是其他类型;（）表示空元组
a = ()
print(type(a))  #<class 'tuple'>
b = ('hello')
print(type(b))  # <class 'str'>
c = (100)
print(type(c))  # <class 'int'>
d = (100,)
print(type(d))  # <class 'tuple'>
e = ('hello',)
print(type(e))  # <class 'tuple'>
