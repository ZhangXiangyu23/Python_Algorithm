# coding:utf-8

# 时间复杂度是O(logN)
def binary(li, left, right, value):
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == value:
            return mid
        if li[mid] < value:
            left = mid + 1
        if li[mid] > value:
            right = mid - 1
    else:
        return -1


# 前提：列表是已经有序的
list_a = [1, 2, 3, 4, 5, 6]
print(binary(list_a, 0, len(list_a) - 1, 8))
