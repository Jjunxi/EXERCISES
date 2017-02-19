#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
' this is   a book  !  '

'  !  book a   is this '
"""

orig = ' this is   a book  !  '
print(orig)
ret = ''
aux = []
idx = 0
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
print(ret)
