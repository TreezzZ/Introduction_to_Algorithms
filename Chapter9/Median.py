# -*- coding:utf-8 -*-

"""寻找近似中位数
"""

import random
from Chapter2.InsertSort import insert_sort


def median(arr, left, right):
    """寻找近似中位数

    Args:
        arr(list): 数组
        left(int): 数组第一个元素下标
        right(int): 数组最后一个元素下标

    Returns:
        med(int): 数组近似中位数
    """
    if left == right:
        return arr[left]
    n = right - left + 1
    group_median = []
    for i in range(0, n, 5):
        left = i
        for j in range(i, i + 5):
            if j < n:
                right = j

        insert_sort(arr, left, right)
        if i + 4 < n:
            group_median.append(arr[i + 2])
        else:
            group_median.append(arr[(n-i)//2])
    med = median(group_median, 0, len(group_median)-1)
    return med


if __name__ == '__main__':
    arr = list(range(1, 1000))
    random.shuffle(arr)
    print(median(arr, 0, len(arr)-1))
