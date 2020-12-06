#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    print("Симметричны ли точки относительно начала координат?")
x1=float(input("Введите х1 "))
y1=float(input("Введите y1 "))
x2=float(input("Введите х2 "))
y2=float(input("Введите y2 "))
if (x1) == abs(x2) and (y1) == abs(y2):
        print("Точки симметричны относительно начала координат")
else:
        print("Точки не симметричны")
