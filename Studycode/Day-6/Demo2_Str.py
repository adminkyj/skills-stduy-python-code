"""
字符串的简单使用2
Version:1.0
Author:x鑫
"""
# 字符的特殊表示：Python允许\后面可以跟一个8进制或16进制来表示字符
# 例如：\141和\x61都代表小字母a,前是8进制，后是16进制
# 还有一种表示字符的方式：在\u后跟Unicode字符编码
s1 = '\141\142\143\x63\x62\x61'
s2 = '\u963f\u946b'
print(s1)  # abccba
print(s2)  # 阿鑫

# 拼接和重复
s1 = 'hello' + ',' + 'world'
print(s1)  # hello,world
s2 = '@#' * 3
print(s2)  # @#@#@#
s1 += s2
print(s1)  # hello,world@#@#@#
s1 *= 2
print(s1)  # hello,world@#@#@#hello,world@#@#@#
# 分割线
print("-------------------------------------------------")

# 比较运算：俩个字符串类型的变量可以直接使用比较运算来判断俩字符串的相等性大小
# 需要注意的是，字符串大小比较比的是每一个字符对应的编码的大小。
# 例如：A的编码是65，a的编码是97，所以a>A的结果会是True
# 而当第一个或者往后的大小对等时，会比较后一位大小，直到分出胜负
# 例如：boy<bad中实际比较的时o和a的编码大小，结果时False
# 补充：可用ord函数获取字符的大小。
s1 = 'a whole new world'
s2 = 'hello world'
print(s1 == s2)
print(s1 < s2)
print(s1 == 'hello world')
print(s2 == 'hello world')
print(s2 != 'Hello world')
s3 = '阿鑫'
print(ord('阿'))  # 38463
print(ord('鑫'))  # 37995
s4 = '易水城'
print(ord('易'))  # 26131
print(ord('水'))  # 27700
print(ord('城'))  # 22478
print(s3 >= s4)
print(s3 != s4)
# 分割线
print("-------------------------------------------------")

# 成员运算：在Python中可用in和not in 判断一个字符串中是否包含另一个字符或字符串，与列表一样
# in 和not in 称为成员运算，返回布尔类型
s1 = 'hello,world'
s1 = 'goodbye,world'
print('wo' in s1)  # True
print('wo' not in s1)  # False
print(s2 in s1)  # False

# 获取字符串长度：使用内置函数len
a = 'hello,world'
print(len(a))  # 11
print(len('goodbye,world'))  # 13

# 索引和切片说明：字符串的索引和切片操作跟列表、元组几乎没区别，因为字符串也是一种有序序列，可通过正向或反向的整数索引访问其元素
# 需要注意的是：字符串是不可变类型，所以不能通过索引运算修改字符串中的字符
str1 = 'abc123456'
n = len(str1)
print(str1[0], str1[-n])  # a a
print(str1[n - 1], str1[-1])  # 6 6
print([str1], str1[-7])  # c c
print(str1[5], str1[-4])  # 3 3
print(str1[2:5])  # c12
print(str1[-7:-4])  # c12
print(str1[2:])  # c123456
print(str1[:2])  # ab
print(str1[::2])  # ac246
print(str1[::-1])  # 654321cba
