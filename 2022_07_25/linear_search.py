# coding:utf-8

"""
    输入一个列表和一个值
    查找这个值在列表中的索引位置，如果在列表中没有找到，则返回-1
"""

def linear(li, value):
    for index, v in enumerate(li):
        if v == value:
            return index
    else:
        return -1


# 时间复杂度O(N)
if __name__ == "__main__":
    list_one = [5, 8, 10, 3, 2, 1]
    print(linear(list_one, 88))
