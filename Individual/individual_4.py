# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

if __name__ == '__main__':
    x = float(input("Enter x> "))

    EPS = 10 ** -10

    a = x
    S, k = a, 0

    while math.fabs(a) > EPS:
        a *= (x ** 2 * (2 * k + 1) ** 2) / ((2 * k + 3) ** 2)
    S += a
    k += 1

    print(f"Shi({x}) = {S}")
