#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import sys
EPS = 1e-10
if __name__ == '__main__':
    x = float(input("Введите x "))
    if x == 0:
        print("Ошибка! Значение х не может равняться 0 ", file=sys.stderr)
        exit(1)
    a = x
    S, n = a, 1
    while math.fabs(a) > EPS:
        a *= (x ** (2 * n + 1)) / ((2 * n + 1)*(2 * n+ 1))
        S += a
        n += 1
    print(f"Ei({x}) = {S}")
