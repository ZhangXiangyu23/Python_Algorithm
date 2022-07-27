# coding:utf-8

"""
    linear_search
"""

def linear_search(li, value):
    for index, v in enumerate(li):
        if v == value:
            return index
    else:
        return -1

li = [8, 2, 1, 0, 12, -8]
print(linear_search(li, 100))
