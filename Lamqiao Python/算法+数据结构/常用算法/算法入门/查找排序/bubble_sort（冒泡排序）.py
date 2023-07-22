# _*_coding:utf-8_*_
# created by Alex Li on 11/5/17

import random
from cal_time import *

@cal_time
def bubble_sort(li):
    for i in range(len(li)-1):  #第i趟
        exchange = False
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        if not exchange:
            return


li = list(range(10000))
random.shuffle(li)

bubble_sort(li)
