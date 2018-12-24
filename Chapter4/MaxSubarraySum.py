# -*- coding:utf-8 -*-


def max_subarray_sum(arr, *args):
    """最大子数组和问题。给定一个数组，求最大子数组的和。

    Args:
        arr(list): 给定数组
        args(tuple): (left, right)数组第一个元素下标和数组最后一个元素下标

    Returns:
        max_sum(int): 最大子数组和
    """
    assert len(args) == 0 or len(args) == 2
    if len(args) == 0:
        return max_subarray_sum(arr, 0, len(arr)-1)

    left, right = args
    if left == right:
        return arr[left]

    assert left < right

    mid = left + (right - left) // 2

    # 左半数组最大子数组和
    left_sum = max_subarray_sum(arr, left, mid)

    # 右半数组最大子数组和
    right_sum = max_subarray_sum(arr, mid+1, right)

    # 跨越左右数组的最大子数组和
    cross_sum = max_cross_subarray_sum(arr, left, mid, right)

    # 取三者中最大为最大子数组和
    return max(left_sum, right_sum, cross_sum)


def max_cross_subarray_sum(arr, left, mid, right):
    """跨越左右子数组的最大子数组和

    Args:
        arr(list): 给定数组
        left(int): 数组第一个元素下标
        mid(int): 数组中间下标
        right(int): 数组最后一个元素下标

    Returns:
        max_sum(int): 最大子数组和
    """
    # 从中间开始向左扫描，求左半边最大和
    left_max, sum_value = 0, 0
    for i in range(mid, left-1, -1):
        sum_value += arr[i]
        if sum_value > left_max:
            left_max = sum_value

    # 从中间开始向右扫描，求右半边最大和
    right_max, sum_value = 0, 0
    for i in range(mid+1, right+1):
        sum_value += arr[i]
        if sum_value > right_max:
            right_max = sum_value

    return left_max + right_max


if __name__ == '__main__':
    arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print(max_subarray_sum(arr))
