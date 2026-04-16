"""
分支结构
if-elif-else的简单使用
version:1.0
Author:x鑫
"""

"""
# BMI计算器
height = float(input('身高(cm)：'))
weight = float(input('体重(kg):'))
bmi = weight / (height / 100) ** 2
print(f"{bmi=: .1f}")
if 18.5 < bmi:
    print("你的体重跟瘦猴似的！")
elif bmi < 24:
    print("你的身体没毛病！")
elif bmi < 27:
    print("你的体重过重！")
elif bmi < 30:
    print("猪神降世！")
else:
    print("卡车来咯！！")
# 分割线
print("------------------------------------------------------------------")

"""

"""
match与case分支结构
"""
status_code = int(input("响应状态码："))
match status_code:
    case 400: description = "Bad Request"
    case 401: description = "Unauthorized"
    case 403: description = "Forbidden"
    case 404: description = "Not Found"
    case 405: description = "Method Not Allowed"
    case 418: description = "I am teapot"
    case 429: description = "Too many requests"
    case _: description = "Unknown Status Code"
print("状态码描述：",description)

