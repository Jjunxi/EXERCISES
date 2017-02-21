#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
matrix exercises
多维列表
"""

from common import *
import random
import numpy as np


def generate_matrix(row_num, col_num, is_random=False):
    rst = []
    if is_random:
        rst = [[random.randint(1, row_num * col_num + 1) for i in range(col_num)] for i in range(row_num)]
    else:
        rst = np.arange(1, row_num * col_num + 1).reshape(row_num, col_num)
    print(rst)
    return rst


# B[i][j] = A[0][0] + ... + A[i][j]
def my_sum(matrix):
    row_num = len(matrix)
    col_num = len(matrix[0])

    # 构造多维列表时，一行一行构造
    rst = []
    for i in range(row_num):
        line = []
        for j in range(col_num):
            l = [matrix[x][y] for x in range(i + 1) for y in range(j + 1)]
            line.append(sum(l))
        rst.append(line)
    print(rst)
    return rst


# transpose
def transpose(matrix):
    col_num = len(matrix[0])
    rst = [[x for x in matrix[:, i]] for i in range(col_num)]
    print(rst)
    return rst


def spiral_order(matrix):
    pass


def demo():
    org = generate_matrix(2, 3, True)
    my_sum(org)

    org = generate_matrix(3, 5)
    transpose(org)


def main():
    try:
        try:
            demo()
        except Exception as e:
            raise Usage(e)
    except Usage as usg:
        Usage.show_info()
        return -1


if __name__ == "__main__":
    sys.exit(main())
