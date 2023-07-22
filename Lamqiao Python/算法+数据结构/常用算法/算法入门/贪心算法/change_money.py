#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/4/14

t = [100, 50, 20, 5]

def change(t, n):
    m = [0 for _ in range(len(t))]
    for i, money in enumerate(t):
        m[i] = n // money
        n = n % money
    return m, n

print(change(t, 376))