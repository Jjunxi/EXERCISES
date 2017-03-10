#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
description
"""

from common import *
from PIL import Image
import time
import glob
import subprocess


def demo():
    # handle here
    path = "D:\MYPYTHONS\EXERCISES\\files\\"
    for infile in glob.glob(path + '*.jpg'):
        print(infile)
        image = Image.open(infile)
        image.show()
        #viewer = subprocess.Popen(['some_viewer', infile])
        #viewer.terminate()
        #viewer.kill()


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
