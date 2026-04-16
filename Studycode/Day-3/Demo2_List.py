"""
用列表方法对列表进行简单的操作1
Version:1.0
Author:x鑫
"""
# 添加和删除元素
languages = ["Python", "C++", "C#", "C++", "C++"]
languages.append('Java')  # 添加元素，默认在尾部
print(languages)
languages.insert(2, "Go")  # 在 2 下标插入元素
print(languages)
# 删除用if配合，防止访问越界，导致列表崩溃
if "C++" in languages:
    languages.remove("C++")  # 当列表里有多个相同元素时，删除第一个元素
if "asdf" in languages:
    languages.remove("asdf")
print(languages)
# 删除也可以用pop方法，通过“有效”下标删除元素，"无效"下标会引起“下标错误异常”
# pop不给下标，将会默认删除最后一个元素
languages.pop(0)
print(languages)
languages.pop(2)
print(languages)
# pop删除方法时，会返回被删除的元素
num = languages.pop(0)
print(num)


