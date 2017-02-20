#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
customized exception handling
"""

import traceback


class Usage(Exception):
    def __init__(self, ex):
        self.ex = ex
        self.info = '***Exception*** \n' + str(ex)

    def show_info(self):
        traceback.print_exc()
