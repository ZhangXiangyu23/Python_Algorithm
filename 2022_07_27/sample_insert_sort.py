# coding:utf-8

"""
    sample_insert_sort
"""

def sample_insert_sort(li):
    cursor = 0
    for i in range(1, len(li)):
        temp = li[i]
        flag = False
        while temp < li[cursor] and cursor >= 0:
            li[cursor+1] = li[cursor]
            cursor = cursor - 1
            flag = True
        if flag:
            li[cursor+1] = temp
        cursor = i

if __name__ == "__main__":
    li = [10, -2, 6, 4, 10, -8]
    print("排序之前", li)
    sample_insert_sort(li)
    print("排序之后", li)



