#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
customized exception handling
"""


class Usage(Exception):
    def __init__(self, ex):
        self.ex = ex
        self.info = '***Exception*** \n' + str(ex)
