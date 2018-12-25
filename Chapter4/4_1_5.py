# -*- coding:utf-8 -*-
"""练习4.1-5 线性时间内求出最大子数组
"""


def linear_max_subarray_sum(arr):
    """线性时间内求出最大子数组和，动态规划思想。max_sum[k] = max(sum[k-1]+arr[k], arr[k])，要么前一项的最大子数组和加上目前要处理的
    一项构成新的最大子数组和，要么新的一项单独构成一个最大子数组和的起点。

    Args:
        arr(list): 数组

    Returns:
        max_sum(int): 最大子数组和
    """
    sum_record = list()
    sum_record.append(0)
    max_sum = 0

    for i in range(len(arr)):
        sum_record.append(max(sum_record[i]+arr[i], arr[i]))
        if sum_record[-1] > max_sum:
            max_sum = sum_record[-1]

    return max_sum


if __name__ == '__main__':
    arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print(linear_max_subarray_sum(arr))