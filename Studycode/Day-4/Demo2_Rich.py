import random
from rich.console import Console
from rich.table import Table
"""
rich库
优点：可以帮助我们用最简单的方式产生最漂亮的输出
Version:1.0
Author:x鑫
"""

# 创建控制台
console = Console()
n = int(input("生成几注号码："))
red_balls = [i for i in range(1,34)]
blue_balls = [i for i in range(1,17)]

# 创建表格并添加表头
table = Table(show_header=True)
for col_name in ('序号','红球','篮球'):
    table.add_column(col_name,justify='center')
for i in range(n):
    selected_balls = random.sample(red_balls,6)
    selected_balls.sort()
    blue_ball = random.choice(blue_balls)
    # 向表格中添加（序号、红色球、蓝色球）
    table.add_row( # 每一列用逗号隔开：列1，列2，列3
        str(i + 1),
        f'[red]{"--".join([f"{ball:0>2d}" for ball in selected_balls])}[/red]',
        f'[blue]{blue_ball:0>2d}[/blue]'
        # join()里面用列表生成式将红球号码处理成字符串并存到一个列表中
        # ” “.join()  是将列表中的多个字符串用空格拼接成一个完整的字符串
        # [red]...[/red]用来设置颜色为红色
    )
# 通过控制台输出表格
console.print(table)

