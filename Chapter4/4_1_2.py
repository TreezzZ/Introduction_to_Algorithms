# -*- coding:utf-8 -*-
"""
练习4.1-2 编写暴力求解最大子数组问题
"""


def bruce_max_subarray_sum(arr):
    """暴力求解最大子数组和
    Args:
        arr(list): 数组

    Returns:
        max_sum(int): 最大子数组和
    """
    max_sum = 0
    for i in range(len(arr)):
        epoch_sum = 0
        for j in range(i, len(arr)):
            epoch_sum += arr[j]
            if epoch_sum > max_sum:
                max_sum = epoch_sum

    return max_sum


if __name__ == '__main__':
    arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print(bruce_max_subarray_sum(arr))