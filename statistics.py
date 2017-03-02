#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
统计数字在序列中出现的次数
"""

from common import *
from collections import Counter


def demo(data):
    rst = dict.fromkeys(data, 0)
    for x in data:
        rst[x] += 1
    print(rst)


def demo_v1(data):
    rst = dict(Counter(data))
    print(rst)
    print(rst[6])


def main():
    try:
        try:
            data = [randint(0, 20) for _ in range(30)]
            print(data)
            demo(data)
            demo_v1(data)
        except Exception as e:
            raise Usage(e)
    except Usage as usg:
        Usage.show_info()
        return -1


if __name__ == "__main__":
    sys.exit(main())
