# _*_coding:utf-8_*_
# created by Alex Li on 12/3/17

from cal_time import *

@cal_time
def count_sort(li, max_count=100):
    count = [0 for _ in range(max_count+1)]
    for val in li:
        count[val] += 1
    li.clear()
    for ind, val in enumerate(count):
        for i in range(val):
            li.append(ind)

@cal_time
def sys_sort(li):
    li.sort()

import random, copy
li = [random.randint(0,100) for _ in range(100000)]

li1 = copy.deepcopy(li)
li2 = copy.deepcopy(li)

count_sort(li1)
sys_sort(li2)