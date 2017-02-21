#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
matrix exercises
多维列表
B[i][j] = A[0][0] + ... + A[i][j]
"""

from common import *
import random

ROW_NUM = 3
COL_NUM = 2


def my_sum(matrix):
    # 构造多维列表时，一行一行构造
    rst = []
    for i in range(ROW_NUM):
        line = []
        for j in range(COL_NUM):
            l = [matrix[x][y] for x in range(i + 1) for y in range(j + 1)]
            line.append(sum(l))
        rst.append(line)
    return rst


def demo():
    matrix = [[random.randint(1, 9) for i in range(COL_NUM)] for i in range(ROW_NUM)]
    print(matrix)
    print(my_sum(matrix))


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
