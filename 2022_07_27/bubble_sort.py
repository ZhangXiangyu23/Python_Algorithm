# coding:utf-8

"""
    冒泡排序
"""

li = [3, 9, 12, -5, 6, 2]
print("排序之前", li)

def bubble_test(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                temp = li[j]
                li[j] = li[j+1]
                li[j+1] = temp

bubble_test(li)
print("排序之后", li)