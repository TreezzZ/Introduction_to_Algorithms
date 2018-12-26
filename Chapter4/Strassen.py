# -*- coding:utf-8 -*-

"""Strassen算法求矩阵乘法
"""

import numpy as np


def strassen(A, B):
    """Strassen算法求矩阵乘法

    Args:
        A(np.array): 矩阵1
        B(np.array): 矩阵2

    Return:
        C(np.array): 矩阵乘法结果
    """
    n, _ = A.shape

    if n == 1:
        C = np.array(A[0, 0] * B[0, 0])
        return C
    else:
        A11 = A[0:n//2, 0:n//2]
        A12 = A[0:n//2, n//2:]
        A21 = A[n//2:, 0:n//2]
        A22 = A[n//2:, n//2:]
        B11 = B[0:n//2, 0:n//2]
        B12 = B[0:n//2, n//2:]
        B21 = B[n//2:, 0:n//2]
        B22 = B[n//2:, n//2:]

        S1 = B12 - B22
        S2 = A11 + A12
        S3 = A21 + A22
        S4 = B21 - B11
        S5 = A11 + A22
        S6 = B11 + B22
        S7 = A12 - A22
        S8 = B21 + B22
        S9 = A11 - A21
        S10 = B11 + B12

        P1 = strassen(A11, S1)
        P2 = strassen(S2, B22)
        P3 = strassen(S3, B11)
        P4 = strassen(A22, S4)
        P5 = strassen(S5, S6)
        P6 = strassen(S7, S8)
        P7 = strassen(S9, S10)

        C11 = P5 + P4 - P2 + P6
        C12 = P1 + P2
        C21 = P3 + P4
        C22 = P5 + P1 - P3 - P7

        C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
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

    print(strassen(A, B))
