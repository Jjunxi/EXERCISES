#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
comprehension exercises
列表解析是按要求生成列表
"""

from common import *


# 请编写一个函数，它接受一个 list，然后把list中的所有字符串变成大写后返回，非字符串元素将被忽略。
def to_uppers(org):
    return [x.upper() for x in org if isinstance(x, str)]


# 找出对称的 3 位数。例如，121 就是对称数
def symmetry():
    return [x * 100 + y * 10 + x for x in range(1, 10) for y in range(0, 10)]


def demo():
    #  1-100 并打印出7的倍数
    rst = [x for x in range(1, 101) if x % 7 == 0]
    # 生成列表 [1x2, 3x4, 5x6, 7x8, ..., 99x100]
    rst = [x * (x + 1) for x in range(1, 100, 2)]
    print(to_uppers(['Hello', 'world', 101]))
    print(symmetry())


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
