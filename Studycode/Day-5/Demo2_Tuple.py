"""
元组的简单使用
Version:1.0
Author:x鑫
"""
# 打包和解包的操作
# 当我们用多个逗号分隔开的值赋给一个变量时，它们会打包成一个元组类型
# 当我们把一个元组赋值给多个变量时，元组会解包多个值，然后分给变量
# 打包操作：
a = 10, 25, 77
print(type(a))
print(a)
# 解包操作：
i, j, k, = a
print(i, j, k)
# 需要注意的是，当你解包出来的元素个数和变量个数不对等时候，会引发异常。
# 错误信息：too many values to unpack(解包的值太多)或not enough values to unpack(解包的值不足)
a = 1, 10, 100, 1000
# i,j,k=a  # ValueError: too many values to unpack (expected 3)
# i,j,k,l,m,n,=a  #ValueError: not enough values to unpack (expected 6, got 4)
print('---------------------------------')
# 解决数量个数不对等的方法：用星号表达式
# 星号表达式:可以让一个变量接受多个值，变成列表类型
# 需要注意的是，在解包语法中星号表达式只能出现一次
a = 1, 10, 100, 1000
i, j, *k = a
print(i, j, k)  # 1 10 [100, 1000]
i, *j, k = a
print(i, j, k)  # 1 [10, 100] 1000
*i, j, k = a
print(i, j, k)  # [1, 10] 100 1000
*i, j = a
print(i, j)  # [1, 10, 100] 1000
i, *j = a
print(i, j)  # 1 [10, 100, 1000]
i, j, k, *l = a
print(i, j, k, l)  # 1 10 100 [1000]
i, j, k, l, *m = a
print(i, j, k, l, m)  # 1 10 100 1000 []

# 解包语法对所有的序列都成立，说明前面的列表、range函数构造的范围甚至字符串都可以用”解包语法“
a, b, *c = range(1, 10)
print(a, b, c)  # 1 2 [3, 4, 5, 6, 7, 8, 9]
a, b, c = [1, 10, 110]
print(a, b, c)  # 1 10 110
a, *b, c = 'hello'
print(a, b, c)  # h ['e', 'l', 'l'] o

"""
元组和列表的比较
元组是不可变类型，不可变类型更适合多线程环境，因为它降低了并发访问变量的同步化开销
元组是不可变类型，通常不可变类型在创建时间上要优于对应的可变类型。
"""
# 用timeit模块来看创建保存相同的元素的元组和列表各自花费的时间
# 每个操作执行10000000次:一千万次
import timeit

print('%.4f' % timeit.timeit('[1,2,3,4,5,6,7,8,9]', number=10000000))  # 0.3707秒
print('%.4f' % timeit.timeit('(1,2,3,4,5,6,7,8,9)', number=10000000))  # 0.0666

# 元组和列表的类型可以相互转换
infos = ('a鑫', 45, True, '广东揭阳')
print(list(infos))  # ['a鑫', 45, True, '广东揭阳']
frts = ('apple', 'banana', 'orange')
print(tuple(frts))  # ('apple', 'banana', 'orange')
