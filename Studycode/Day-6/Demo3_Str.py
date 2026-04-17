"""
字符串的简单使用3
Version:1.0
Author:x鑫
"""
s1 = 'hello,world!'
# 字符串首字母大写
print(s1.capitalize())
# 字符串每个单词首字母大写
print(s1.title())
# 字符串变大写
print(s1.upper())
s2 = 'GOODBYE'
print(s2.lower())  # 字符串变小写
# 检查值
print(s1)
print(s2)

# 查找操作：在一个字符串中查找另一个字符串，可用字符串的find和index方法；可通过参数来指定查找范围
s3 = 'hello,world'
print(s3.find('or'))  # 7
print(s3.find('or', 10))  # -1
print(s3.find('of'))  # 1
print(s3.index('or'))  # 7
# print(s3.index('or',9))  # ValueError: substring not found
# 当find找不到指定字符串时会返回 -1;当index找不到指定字符串时会报错：ValueError: substring not found
print("----------------------------")

# find和index的逆向查找（后往前）：rfind和rindex
s4 = 'hello,world'
print(s4.find('o'))  # 4
print(s4.rfind('o'))  # 7
print(s4.rindex('o'))  # 7
# print(s4.rindex('o',8))  # ValueError: substring not found

# 性质判断：可通过字符串的startswith或endswith来判断字符串是否以某个字符串开头或结尾
# 还可用is判断字符串特征，俩者都是返回布尔值
s5 = 'hello,world!'
print(s5.startswith("He"))  # False
print(s5.startswith("hel"))  # True
print(s5.endswith("!"))  # True
s6 = 'abc123456'
print(s2.isdigit())  # False;  isdigit判断是否完全由数字构成的
print(s2.isalpha())  # True;  isalpha判断是否完全由字母构成的
print(s2.isalnum())  # True;  isalnum判断是否由字母和数字构成的
print("----------------------------")

# 格式化：在python中，字符串类型可通过center\ljust\rjust方式居中、左对齐和右对齐处理
# 如要在字符串左侧补零，也可用zfill方法
s7 = 'hello,world！'
print(s7.center(20, '*'))  # ****hello,world！****
print(s7.rjust(20))
print(s7.ljust(20))
print('33'.zfill(5))  # 00033
print('-33'.zfill(5))  # -0033

# 格式化
a = 321
b = 123
print('%d * %d = %d' % (a, b, a * b))
print('{0} * {1} = {2}'.format(a, b, a * b))
# python3.6开始有更简洁的方式
print(f'{a} * {b} = {a * b}')
print("----------------------------")
"""
变量值	    占位符	    格式化结果	    说明
3.1415926	{:.2f}	    '3.14'	        保留小数点后两位
3.1415926	{:+.2f} 	'+3.14'	        带符号保留小数点后两位
-1	        {:+.2f}	    '-1.00'	        带符号保留小数点后两位
3.1415926	{:.0f}	    '3'	            不带小数
123	        {:0>10d}	'0000000123'	左边补0，补够10位
123	        {:x<10d}	'123xxxxxxx'	右边补x ，补够10位
123	        {:>10d}	    '       123'	左边补空格，补够10位
123     	{:<10d}	    '123       '	右边补空格，补够10位
123456789	{:,}	    '123,456,789'	逗号分隔格式
0.123	    {:.2%}e	    '12.30%'	    百分比格式
123456789	{:.2}	    '1.23e+08'	    科学计数法格式
"""

# 修剪方式：字符串的strip方法可帮我们拿到将原字符串修建掉左右俩段指定字符之后的字符串，默认为修建空格
# strip还有俩种版本：lstrip和rstrip
s7 = '                    wyxadmin2023@126.com       '
print(s7.strip())
s8 = '~一个人究竟能创造多少价值~'
print(s8.rstrip('~'))  # ~一个人究竟能创造多少价值
print(s8.lstrip('~'))  # 一个人究竟能创造多少价值~

# 替换方式：将新内容替换字符串中指定的内容,可用replace方法
# replace有三个参数：第一个是被替换内容，第二个是替换后的内容，第三个是指定替换参数的次数
s9 = 'hello,good world'
print(s9.replace('o', "@"))  # hell@,g@@d w@rld
print(s9.replace('o', "@", 3))  # hell@,g@@d world
print("----------------------------")

# 拆分与合并：split方法和join方法，前者将字符串拆为多个字符串返回一个列表，后者将多个字符串连接成一个字符串
s10 = "I love you"
words = s10.split()
print(words)  # ['I', 'love', 'you']
print('--'.join(words))  # I--love--you
# split默认用空格进行拆分，当然也可以用指定字符进行拆分,还可以指定最大拆分次数来控制拆分效果
s11 = "I@love@you@so@much"
words = s11.split("@")
print(words)  # ['I', 'love', 'you', 'so', 'much']
words = s11.split('@', 2)
print(words)  # ['I', 'love', 'you@so@much']

# 编码和解码
# Python中除了字符串str类型外，还有一种表示二进制数据的字节串类型。
# 字节串：由零个或多个字节组成的有限序列。
# 通过encode方法，按照某种编码方式将字符串编码为字节串
# 也可以用字节串的decode方法，将字节串解码为字符串
a = '阿鑫'
b = a.encode('utf-8')
c = a.encode('gbk')
print(b)  # b'\xe9\x98\xbf\xe9\x91\xab'
print(c)  # b'\xb0\xa2\xf6\xce'
print(b.decode('utf-8'))
print(c.decode('gbk'))
# 需要注意的是，如果编码和解码的方式不一致将会导致乱码（无法再现原始内容）或引发UnicodeDecodeError错误
