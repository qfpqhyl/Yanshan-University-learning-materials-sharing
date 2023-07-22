#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/9/9


# 子问题的重复计算
def fibnacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibnacci(n-1) + fibnacci(n-2)


# 动态规划（DP）的思想 = 递推式 + 重复子问题
def fibnacci_no_recurision(n):
    f = [0,1,1]
    if n > 2:
        for i in range(n-2):
            num = f[-1] + f[-2]
            f.append(num)
    return f[n]

print(fibnacci_no_recurision(100))