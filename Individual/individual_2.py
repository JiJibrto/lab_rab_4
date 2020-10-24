# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys

if __name__ == '__main__':
    x_a = int(input("Enter x1> "))
    y_a = int(input("Enter y1> "))
    x_b = int(input("Enter x2> "))
    y_b = int(input("Enter y2> "))
    r_a = int(input("Enter r1> "))
    r_b = int(input("Enter r2> "))

# math.exp don't work and i don't know why /(-_-*)\

    l = math.floor(math.sqrt(math.fabs(x_a-x_b) * math.fabs(x_a-x_b) + math.fabs(y_a-y_b) * math.fabs(y_a-y_b)))

    if x_a == x_b and y_a == y_b and r_b == r_a:
        print("There's endless set point's of intersection of a circle's")
    elif x_a == x_b and y_a == y_b and r_a != r_b:
        print("There's none point of intersection of a circle")
    elif l < (r_a + r_b):
        print("There's two point's of intersection of a circle's")
    elif l == (r_a + r_b):
        print("There's one point of intersection of a circle's")
    else:
        print("There's none point of intersection of a circle")