#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
description
"""

from common import *


def demo():
    # handle here
    pass


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
