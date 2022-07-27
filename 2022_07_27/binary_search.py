# coding:utf-8

"""
    binary_search
"""

def binary_search(li, value):
    left = 0
    right = len(li)-1
    while left <= right:
        mid = (left + right) // 2
        if value == li[mid]:
            return mid
        elif value > li[mid]:
            left = mid + 1
        else:
            right = mid - 1
    else:
        return -1


# 使用binary_search应该提前排好序
li = [1, 2, 3, 4, 5, 6, 7]

print(binary_search(li, 5))
