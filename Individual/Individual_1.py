# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys

if __name__ == '__main__':
    a = int(input("Enter the cost of wallpaper> "))
    b = int(input("Enter the cost of a can of paint> "))
    s = 8 * a + b * 2

    if s > 1000:
        s *= 0.91
    elif s > 800:
        s *= 0.93
    elif s > 500:
        s *= 0.95
    elif s > 200:
        s *= 0.97

    print(f"\nAll cost = {s}")