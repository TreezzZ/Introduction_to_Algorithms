# -*- coding:utf-8 -*-

"""插入排序
"""


def insert_sort(arr, left, right):
    """插入排序

    Args:
        arr(list): 数组
        left(int): 数组第一个元素下标
        right(int): 数组最后一个元素下标
    """
    for i in range(left+1, right+1):
        tmp = arr[i]
        j = i
        while j > left and tmp < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = tmp


if __name__ == '__main__':
    arr = [3, 2, 1, 5, 4, 6, 0]
    insert_sort(arr, 0, 3)

    print(arr)
