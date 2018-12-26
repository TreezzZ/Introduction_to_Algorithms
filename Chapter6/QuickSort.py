# -*- coding:utf-8 -*-

"""快速排序
"""

import random


def quick_sort(arr, left, right):
    """快速排序

    Args:
        arr(list): 数组
        left(int): 数组第一个元素下标
        right(int): 数组最后一个元素下标
    """
    if left < right:
        pivot = random_partition(arr, left, right)
        quick_sort(arr, left, pivot-1)
        quick_sort(arr, pivot+1, right)


def partition(arr, left, right):
    """划分

    Args:
        arr(list): 数组
        left(int): 数组第一个元素下标
        right(int): 数组最后一个元素下标

    Returns:
        pivot(int): 划分
    """
    pivot = arr[left]
    i, j = left, right

    while i < j:
        while i < j and arr[i] < pivot:
            i += 1
        while i < j and arr[j] > pivot:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
    arr[i] = pivot

    return i


def random_partition(arr, left, right):
    """随机划分

    Args:
        arr(list): 数组
        left(int): 数组第一个元素下标
        right(int): 数组最后一个元素下标

    Returns:
        pivot(int): 划分
    """
    i = random.randint(left, right)
    arr[left], arr[i] = arr[i], arr[left]
    return partition(arr, left, right)


if __name__ == '__main__':
    arr = [3, 2, 5, 1, 4, 7, 9, 0]
    quick_sort(arr, 0, len(arr)-1)
    print(arr)
