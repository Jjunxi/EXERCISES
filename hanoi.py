#!/usr/bin/env python
# -*- coding: utf-8 -*-

count = 0
def hanoi(n, start, end, via):
    if n == 1:
        global count
        count += 1
        print('%s --> %s' % (start, end))
    else:
        hanoi(n-1, start, via, end)
        hanoi(1, start, end, via)
        hanoi(n-1, via, end, start)
    return count

print(hanoi(4, 'A', 'C', 'B'))