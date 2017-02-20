#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
' this is   a book  !  '

'  !  book a   is this '

不是简单的分词，空格需要保留。
"""

from common import *


def reverse_sentence(orig):
    aux = []
    need_append = False

    for ch in orig:
        if not ch.isalpha():
            aux.append(ch)
            need_append = True
        else:
            if need_append:
                aux.append('')
                need_append = False
            # 此处不用idx控制，而是直接用-1对last elem操作
            aux[-1] += ch
    # reverse acts itself and returns None
    aux.reverse()
    ret = ''.join(aux)
    return ret


def demo():
    orig = ' this is   a book  !  '
    print(orig)
    print(reverse_sentence(orig))


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
