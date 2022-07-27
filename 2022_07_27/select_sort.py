# coding:utf-8

"""
    选择排序
"""

li = [9, 2, 6, 5, 6, 1, -5]
print("排序之前", li)
def select_test(li):
    for i in range(len(li)-1):
        for j in range(i+1, len(li)):
            if li[j] < li[i]:
                temp = li[i]
                li[i] = li[j]
                li[j] = temp


select_test(li)
print("排序之后", li)