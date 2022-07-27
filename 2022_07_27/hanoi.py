# coding:utf-8

"""
    递归问题之hanoi
"""

"""
    n为初始柱子的盘子数
    a为初始盘子所在柱子
    b为中转柱子
    c为目的地柱子
"""
def hanoi_test(n, a, b, c):
    if n > 0:
        hanoi_test(n-1, a, c, b)
        print(f"from {a} to {c}")
        hanoi_test(n-1, b, a, c)


# 打印移动过程
hanoi_test(3, 'A', 'B', 'C')