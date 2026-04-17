"""
集合的简单使用
Version:1.0
Author:x鑫
"""
# 创建集合：用{}字面量语法,括号里面至少要有一个元素，否则就不是空集，而是空字典
set1 = {1, 2, 3, 3, 3, 2}
print(set1)  # {1, 2, 3}
set2 = {'banana', 'pitaya', 'apple', 'apple', 'banana', 'grape'}
print(set2)  # {'banana', 'apple', 'pitaya', 'grape'}
set3 = set('hello')
print(set3)  # {'l', 'o', 'h', 'e'}
set4 = set([1, 2, 2, 3, 3, 3, 2, 1])
print(set4)  # {1, 2, 3}
set5 = {num for num in range(1, 20) if num % 3 == 0 or num % 7 == 0}
print(set5)  # {3, 6, 7, 9, 12, 14, 15, 18}
'''
需要注意的是，集合中的元素必须是hashable类型
hashable类型：指的是能够计算出哈希码的数据类型，通常不可变类型都是hashable类型
    例如：整数int、浮点小数float、布尔值bool、字符串str、元组tuple等
可变类型都不是hashable类型
    因为可变类型无法计算本身确定的哈希码，所以它们不能放到集合中。
    例如：不能将列表作为集合中的元素；同样的，由于集合本身也是可变类型，所以集合不能作为集合中的元素。
         我们可以创建嵌套列表（列表的元素也是列表），但不能创建嵌套集合！
'''

# 集合元素的遍历
# 需要注意的是，我们可以用len函数获取集合长度，但是不能通过索引运算来遍历集合中的元素，因为集合元素没有特定的元素
#   不过我们仍可以用for-in实现对集合元素的遍历
set6 = {'Python', 'Java', 'C++', 'Kotlin', 'Swift'}
for elem in set6:
    print(elem)  # 运行结果是无序的
print('----------------------------------------------------')

# 集合的运算(成员运算、交集运算、并集运算、差集运算、比较运算等)

# 成员运算：通过成员运算in和not in 检查元素是否在集合中
set7 = {11, 12, 13, 14, 15}
print(10 in set7)  # False
print(15 in set7)  # True
set8 = {'Python', 'Java', 'C++', 'Swift'}
print('Ruby' in set8)  # False
print('Java' in set8)  # True
print('--------------------------------------------------------')
# 二元运算：主要指的是集合的交集(intersection)、并集(union)、差集(difference)、对称差等运算
set9 = {1, 2, 3, 4, 5, 6, 7}
set10 = {2, 4, 6, 8, 10}
# 交集：拿两个集合重复的元素
print(set9 & set10)  # {2, 4, 6}
print(set9.intersection(set10))  # {2, 4, 6}
# 并集：拿两个集合的所以元素，重复元素只拿一个
print(set9 | set10)  # {1, 2, 3, 4, 5, 6, 7, 8, 10}
print(set9.union(set10))  # {1, 2, 3, 4, 5, 6, 7, 8, 10}
# 差集：假如有一个减数和一个被减数，去拿减数里面没有与被减数重复的数
print(set9 - set10)  # {1, 3, 5, 7}
print(set9.difference(set10))  # {1, 3, 5, 7}
# 对称差：拿俩个集合中不重复的元素
print(set9 ^ set10)  # {1, 3, 5, 7, 8, 10}
print(set9.symmetric_difference(set10))  # {1, 3, 5, 7, 8, 10}
print('----------------------------------------------------------------')

# 需要注意的是：集合的二元运算可以跟赋值运算一起构成“复合赋值运算”
# 例如：set1 |=set2相当于set1 = set1 |set2;与|=相同的方法是update;
#      set1 &=set2相当于set1 = set1 &set2;与&=相同的方法是intersection_update
set11 = {1, 3, 5, 7}
set12 = {2, 4, 6}
set11 |= set12
# set11.update(set12)
print(set11)  # {1, 2, 3, 4, 5, 6, 7}
set13 = {3, 6, 9}
set11 &= set13
# set11.intersection_update(set13)
print(set11)  # {3, 6}
set12 -= set11
# set12.difference_update(set11)
print(set12)  # {2, 4}
print("------------------------------------------------------------")

# 比较运算：俩个集合可用==和!=进行相等性判断，如果其中元素完全相同，就是True，反则False（有不相同的）
# 如果集合A的任意一个元素都是集合B的元素，那集合A就是集合B的子集或者集合B是集合A的超集
# 如果A是B的子集且不等于B，那A就是B的真子集。
# Python中可用<\<=\>\>=来判断;或用issubset和issuperset来判断集合间的关系
set14 = {1, 3, 5}
set15 = {1, 3, 5, 2, 4}
set16 = {1, 3, 2, 5, 4}
print(set14 < set15)  # 判断set14是否为set15的真子集：True
print(set14 <= set15)  # 判断set14是否为set15的子集：True
print(set15 < set16)  # 判断set15是否为set16的真子集：False
print(set15 <= set16)  # 判断set15是否为set16的子集：True
print(set15 > set14)  # 判断set14是否为set15的超集：True
print(set15 == set14)  # False
print('------------------------------------')
print(set14.issubset(set15))  # 判断set14是否为set15的子集：True
print(set15.issuperset(set14))  # 判断set15是否为set14的超集：True

# 集合的方法：已知Python中的集合是可变类型，我们可通过集合的方法向集合添加元素或从集合中移除元素
set17 = {1, 10, 100}
# 添加元素
set17.add(1000)
set17.add(10000)
print(set17)  # {1, 100, 1000, 10, 10000}
# 删除元素
set17.discard(10)
if 100 in set17:
    # remove方法在元素不存在时会引发KeyError错误，因此先用成员运算判断元素是否在集合中
    # 集合还有一个pop方法可用从集合中随机删除一个元素并将删除的元素当返回值返回
    # remove和discard方法只会删除，不会返回被删的值
    set17.remove(100)
print(set17)  # {1, 1000, 10000}
# 清空元素
set17.clear()
print(set17)  # set()
# isdisjoint方法：判断俩集合有没有相同元素，没有返回True，反则False
set18 = {'Java', 'Python', 'C++', 'Kotlin'}
set19 = {'Kotlin', 'Swift', 'Java', 'Dart'}
set20 = {'HTML', 'CSS', 'JavaScript'}
print(set18.isdisjoint(set19))  # False
print(set18.isdisjoint(set20))  # True

'''
不可变集合frozenset
set和frozenset的区别如同list跟tuple的区别
frozenset能够计算出哈希码，因为frozenset时不可变类型
所以frozenset可用作set中的元素
除了不能添加和删除元素,frozenset其他方面与set一样
'''
fset1 = frozenset({1, 3, 5, 7})
fset2 = frozenset(range(1, 6))
print(fset1)  # frozenset({1, 3, 5, 7})
print(fset2)  # frozenset({1, 2, 3, 4, 5})
print(fset1 & fset2)  # frozenset({1, 3, 5})
print(fset1 | fset2)  # frozenset({1, 2, 3, 4, 5, 7})
print(fset1 - fset2)  # frozenset({7})
print(fset1 < fset2)  # False
