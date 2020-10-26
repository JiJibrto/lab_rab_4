# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys

if __name__ == '__main__':
    S = int(input("Enter the amount to pay> "))
    a, b, c, d, e = 0, 0, 0, 0, 0
    temp = 0

    # variable = the number of which notes it shows
    # a = 500
    # b = 100
    # c = 10
    # d = 2
    # e = 1

    while True:
        if S >= 500:
            a = S // 500
            S %= 500
            continue
        elif S >= 100:
            b = S // 100
            S %= 100
            continue
        elif S >= 10:
            c = S // 10
            S %= 10
            continue
        elif S >= 2:
            d = S // 2
            S %= 2
            continue
        elif S >= 1:
            e = S // 1
            S %= 1
            break
        elif S == 0:
            break

    print (f"\n500 - {a}"
           f"\n100 - {b}"
           f"\n10 - {c}"
           f"\n2 - {d}"
           f"\n1 - {e}")

