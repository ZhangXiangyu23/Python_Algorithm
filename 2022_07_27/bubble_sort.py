# coding:utf-8

"""
    冒泡排序
"""
li = [2, 8, -3, 6, 10, -2, 2]
print("排序之前", li)
def bubble_sort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                temp = li[j]
                li[j] = li[j+1]
                li[j+1] = temp

bubble_sort(li)
print("排序之后", li)