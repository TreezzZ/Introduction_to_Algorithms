# -*- coding:utf-8 -*-

"""朴素矩阵乘法，复杂度O(n^3)
"""

import numpy as np


def mul_marix(A, B):
    """朴素矩阵乘法，复杂度O(n^3)

    Args:
        A(np.array): 矩阵1
        B(np.array): 矩阵2

    Return:
        C(np.array): 矩阵乘法结果
    """
    n, _ = A.shape
    C = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            tmp_sum = 0
            for k in range(n):
                tmp_sum += A[i, k] * B[k, j]
            C[i, j] = tmp_sum
    return C


if __name__ == '__main__':
    A = np.array([
        [1, 2, 3, 4],
        [4, 3, 2, 1],
        [1, 3, 5, 7],
        [7, 5, 3, 1],
    ])
    B = np.array([
        [2, 4, 6, 8],
        [8, 6, 4, 2],
        [1, 2, 3, 4],
        [4, 3, 2, 1],
    ])

    print(mul_marix(A, B))
