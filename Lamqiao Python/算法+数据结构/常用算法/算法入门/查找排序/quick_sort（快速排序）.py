# _*_coding:utf-8_*_
# created by Alex Li on 11/5/17

import random
from cal_time import *
import copy
import sys

sys.setrecursionlimit(100000)

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
    if left < right:  # 至少两个元素
        mid = partition(li, left, right)
        _quick_sort(li, left, mid-1)
        _quick_sort(li, mid+1, right)

@cal_time
def quick_sort(li):
    _quick_sort(li, 0, len(li)-1)

li = list(range(100, 0, -1))
# random.shuffle(li)
#
# li1 = copy.deepcopy(li)
# li2 = copy.deepcopy(li)
#
quick_sort(li)
# bubble_sort(li2)
#
# print(li1)
# print(li2)

# li = [9,8,7,6,5,4,3,2,1]
# partition(li, 0, len(li)-1)
print(li)