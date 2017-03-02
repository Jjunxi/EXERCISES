#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
命名元祖
student = ('Ralf', 29, 'male', 'ralf@gmail.com')
"""

from common import *
from collections import namedtuple

'''
NAME = 1
AGE = 2
EMAIL = 3
'''
NAME, AGE, GENDER, EMAIL = range(4)

Role = namedtuple('Role', ['NAME', 'AGE', 'GENDER', 'EMAIL'])


def demo():
    ralf = Role(NAME='Ralf', AGE=29, GENDER='male', EMAIL='ralf@gmail.com')
    print(ralf[NAME])


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
