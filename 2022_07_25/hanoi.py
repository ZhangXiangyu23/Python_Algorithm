# coding:utf-8

"""
    hanoi问题
"""

def hanoi_test(n, a, b, c):
    if n > 0:
        hanoi_test(n-1, a, c, b)
        print(f"disk from {a} to {c}")
        hanoi_test(n-1, b, a, c)


if __name__ == "__main__":
    hanoi_test(3, 'A', 'B', 'C')