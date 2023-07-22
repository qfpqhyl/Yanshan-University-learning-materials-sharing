#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2017/12/10

# O(n) O(kn)
#NB O(nlogn)

from cal_time import *

def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp: #从右面找比tmp小的数
            right -= 1      # 往左走一步
        li[left] = li[right] #把右边的值写到左边空位上
        # print(li, 'right')
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left] #把左边的值写到右边空位上
        # print(li, 'left')
    li[left] = tmp      # 把tmp归位
    return left


def _quick_sort(li, left, right):
    if left<right:  # 至少两个元素
        mid = partition(li, left, right)
        _quick_sort(li, left, mid-1)
        _quick_sort(li, mid+1, right)

@cal_time
def quick_sort(li):
    _quick_sort(li, 0, len(li)-1)

@cal_time
def radix_sort(li):
    max_num = max(li) # 最大值 9->1, 99->2, 888->3, 10000->5
    it = 0
    while 10 ** it <= max_num:
        buckets = [[] for _ in range(10)]
        for var in li:
            # 987 it=1  987//10->98 98%10->8;    it=2  987//100->9 9%10=9
            digit = (var // 10 ** it) % 10
            buckets[digit].append(var)
        # 分桶完成
        li.clear()
        for buc in buckets:
            li.extend(buc)
        # 把数重新写回li
        it += 1


import random,copy

li = [random.randint(0,100000000) for _ in range(100000)]
random.shuffle(li)

li1 = copy.deepcopy(li)
li2 = copy.deepcopy(li)
li3 = copy.deepcopy(li)

quick_sort(li1)
radix_sort(li2)