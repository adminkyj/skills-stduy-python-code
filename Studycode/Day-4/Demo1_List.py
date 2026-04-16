import random
"""
列表的简单练习
Version:1.0
Author:x鑫
"""
# 嵌套列表的简单使用
# 例如：需要保存5个学生3门课程的成绩
scores = [[95, 77, 88],[80, 70, 90],[97, 82, 77],[84, 84,55],[88,69,90]]
print(scores[0])  # [95, 77, 88]
print(scores[0][1])  # 77

# 产生随机数生成5个学生3门课程的成绩
scores = [[random.randrange(60,101) for _ in range(3)] for _ in range(5)]
print(scores)

"""
列表的应用
Version:2.0
Author:x鑫
"""

# 下面我们通过一个双色球随机选号的例子为大家讲解列表的应用。
# 双色球是由中国福利彩票发行管理中心发售的乐透型彩票，每注投注号码由6个红色球和1个蓝色球组成。
# 红色球号码从1到33中选择，蓝色球号码从1到16中选择
red_balls = list(range(34))
selected_balls=[]
# 添加6个红色求到选中列表
for _ in range(6):
    # 生成随机整数代表选中的红色球的下标
    index = random.randrange(len(red_balls))
    # 将选中的球从红色球列表中移除并添加到选中列表
    selected_balls.append(red_balls.pop(index))
# 对选中的红色球排序
selected_balls.sort()
# 输出选中的红色球
for ball in selected_balls:
    print(f"\033[031m{ball:0>2d}\033[0m",end=" ")
    # f"\033[031m---\033[0m"是控制输出内容颜色
    # \033[0m是一个控制码，表示关闭所有属性，就是说前面的控制码会失效
    # m前面的0表示控制台的显示方式为默认值，1表示高亮，5表示闪烁，7表示反闪，30黑色，31红色，32绿色，33黄色，34蓝色
# 随机一个蓝色球
blue_ball = random.randrange(1, 17)
# 输出蓝色球
print(f"\033[034m{blue_ball:0>2d}\033[0m")
print("-------------------------------------------------------------")

# 改良1
red_balls = [i for i in range(1, 34)]
blue_balls = [i for i in range(1, 17)]
# 从红色球列表中随机抽出6个红色球（无放回抽样）
selected_balls = random.sample(red_balls, 6)  # sample（）可实现无返回抽样
# 对选中的红色球排序
selected_balls.sort()
# 输出选中的红色球
for ball in selected_balls:
    print(f"\033[031m{ball:0>2d}\033[0m", end=" ")
# 从蓝色列表中随机抽出1个蓝色球
blue_ball = random.choice(blue_balls)  # choice（）可实现随机抽取一个元素
# 输出蓝色球
print(f"\033[034m{blue_ball:0>2d}\033[0m")

# 改良2：实现随机生成N注号码
n = int(input("生成几注号码："))
red_balls = [i for i in range(1,34)]
blue_balls = [i for i in range(1,17)]
for _ in range(n):
    selected_balls = random.sample(red_balls,6)
    selected_balls.sort()
    for ball in selected_balls:
        print(f"\033[031m{ball:0>2d}\033[0m", end=" ")
    blue_ball = random.choice(blue_balls)
    print(f"\033[034m{blue_ball:0>2d}\033[0m")

