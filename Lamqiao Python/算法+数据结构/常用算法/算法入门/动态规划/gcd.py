#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/9/9


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def gcd2(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a


print(gcd2(12,16))