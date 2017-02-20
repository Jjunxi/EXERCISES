#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
slice exercises
列表切片是按要求提取列表
"""

from common import *


def demo():
    org = list(range(1, 101))
    rst = []
    # 前10个数
    rst = org[:10]
    # 3的倍数
    rst = org[2::3]
    # 不大于50的5的倍数
    rst = org[4:50:5]
    # 最后10个数
    rst = org[-10:]
    # 最后10个5的倍数
    rst = org[54::5]
    print(rst)


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
