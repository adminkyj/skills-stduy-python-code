import random

"""
分支和循环结构实战
Version:1.0
Author:x鑫
"""

# 100以内的素数
# 素数：素数指的是只能被 1 和自身整除的正整数（不包括 1）
#      之前我们写过判断素数的代码，这里相当于是一个升级版本。
print("100内的素数有：")
count = 0
for num in range(2, 101):  #
    isNo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            isNo = False
            break

    if isNo:
        print(f"{num}")
        count += 1
print(f"共计{count}个\t")
# 分割线
print("------------------------------------------------------------------------------------------------")

# 斐波那契数列
# 要求：输出斐波那契数列中的前 20 个数。
# 规律：1, 1, 2, 3, 5, 8, 13, 21, 34, 55
a, b = 0, 1
for _ in range(20):
    a, b = b, b + a
    print(f"{a}", end="\t")
# 分割线
print("\n------------------------------------------------------------------------------------------------")

# 水仙花数
# 要求：找出 100 到 999 范围内的所有水仙花数。
# 是一个 N 位非负整数, 其各位数字的n次方和刚好等于该数本身
for i in range(100, 1000):
    g = i % 10
    s = i // 10 % 10
    b = i // 100
    if (g ** 3) + (s ** 3) + (b ** 3) == i:
        print(i)
# 分割线
print("------------------------------------------------------------------------------------------------")

'''
# //和%的运用
# 将一个不知道有多少位的正整数进行反转 789
n = int(input("请输入一段数字："))
nz = 0
while n != 0:
    nz = nz * 10 + n % 10
    n //= 10
print(nz)
'''

# 百钱百鸡问题
# 公鸡 5 元一只，母鸡 3 元一只，小鸡 1 元三只，用 100 块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
for i in range(0, 21):
    for j in range(0, 33):
        x = 100 - i - j
        if i + x + j == 100 and i * 5 + j * 3 + x / 3 == 100:
            print(f"公鸡{i}只，母鸡{j}只，小鸡{x}只")
# 分割线
print("------------------------------------------------------------------------------------------------")

# CRAPS赌博游戏
# 规则：玩家第一次摇骰子如果摇出了 7 点或 11 点，玩家胜；玩家第一次如果摇出 2 点、3 点或 12 点，庄家胜；
#      玩家如果摇出其他点数则游戏继续，玩家重新摇骰子，如果玩家摇出了 7 点，庄家胜；
#      如果玩家摇出了第一次摇的点数，玩家胜；其他点数玩家继续摇骰子，直到分出胜负。
#      为了增加代码的趣味性，我们设定游戏开始时玩家有 1000 元的赌注，每局游戏开始之前，
#      玩家先下注，如果玩家获胜就可以获得对应下注金额的奖励，如果庄家获胜，玩家就会输掉自己下注的金额。游戏结束的条件是玩家破产（输光所有的赌注）。
money = 1000

while money > 0:
    print(f"当前资产为:{money}")
    while True:
        bet = int(input("请下注："))
        if 0 < bet <= money:
            break
    Opoint = random.randrange(1, 7) + random.randrange(1, 7)
    print(f"玩家第一次掷出来的点数是：{Opoint}")
    if Opoint == 7 or Opoint == 11:
        print("玩家赢！")
        money += bet
    elif Opoint == 2 or Opoint == 3 or Opoint == 12:
        print("庄家赢！")
        money -= bet
    else:
        while True:
            FastPoint = random.randrange(1, 7) + random.randrange(1, 7)
            print(f"玩家掷出来的点数是：{FastPoint}")
            if FastPoint == Opoint:
                print("玩家赢！")
                money += bet
                break
            elif FastPoint == 7:
                print("庄家赢！")
                money -= bet
                break
    if money == 0:
        print("你已经破产！")
        break
