# coding:utf-8

"""
    选择排序
"""
li = [2, -5, 3, 6, -5, 12]
print("排序之前", li)
def select_sort(li):
    for i in range(len(li)-1):
        for j in range(i+1, len(li)):
            if li[j] < li[i]:
                temp = li[i]
                li[i] = li[j]
                li[j] = temp
select_sort(li)
print("排序之后", li)