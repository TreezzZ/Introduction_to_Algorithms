# -*- coding:utf-8 -*-

"""选择第k小数
"""

from Chapter6.QuickSort import random_partition


def select_kth(arr, left, right, k):
    """选择第k小数

    Args:
        arr(list): 数组
        left(int): 数组第一个元素下标
        right(int): 数组最后一个元素下标
        k(int): 选择第k小个数

    Returns:
        kth(int): 第k小个数
    """
    if left == right:
        return arr[left]
    pivot = random_partition(arr, left, right)
    n = pivot - left + 1
    if n == k:
        return arr[pivot]
    elif k < n:
        return select_kth(arr, left, pivot-1, k)
    else:
        return select_kth(arr, pivot+1, right, k-n)


if __name__ == '__main__':
    arr = [3, 7, 1, 4, 2, 5, 6]
    print(select_kth(arr, 0, len(arr)-1, 4))
