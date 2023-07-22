# _*_coding:utf-8_*_
# created by Alex Li on 12/3/17

from cal_time import *

def insert_sort_gap(li, gap):
    for i in range(gap, len(li)): #i 表示摸到的牌的下标
        tmp = li[i]
        j = i - gap #j指的是手里的牌的下标
        while j >= 0 and li[j] > tmp:
            li[j+gap] = li[j]
            j -= gap
        li[j+gap] = tmp

@cal_time
def shell_sort(li):
    d = len(li) // 2
    while d >= 1:
        insert_sort_gap(li, d)
        d //= 2

@cal_time
def insert_sort(li):
    for i in range(1, len(li)): #i 表示摸到的牌的下标
        tmp = li[i]
        j = i - 1 #j指的是手里的牌的下标
        while j >= 0 and li[j] > tmp:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp


def sift(li, low, high):
    """
    :param li: 列表
    :param low: 堆的根节点位置
    :param high: 堆的最后一个元素的位置
    :return: 
    """
    i = low # i最开始指向根节点
    j = 2 * i + 1 # j开始是左孩子
    tmp = li[low] # 把堆顶存起来
    while j <= high: # 只要j位置有数
        if j + 1 <= high and li[j+1] > li[j]: # 如果右孩子有并且比较大
            j = j + 1  # j指向右孩子
        if li[j] > tmp:
            li[i] = li[j]
            i = j           # 往下看一层
            j = 2 * i + 1
        else:       # tmp更大，把tmp放到i的位置上
            li[i] = tmp     # 把tmp放到某一级领导位置上
            break
    else:
        li[i] = tmp  # 把tmp放到叶子节点上

@cal_time
def heap_sort(li):
    n = len(li)
    for i in range((n-2)//2, -1, -1):
        # i表示建堆的时候调整的部分的根的下标
        sift(li, i, n-1)
    # 建堆完成了
    for i in range(n-1, -1, -1):
        # i 指向当前堆的最后一个元素
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1) #i-1是新的high


import random,copy

li = list(range(100000))
random.shuffle(li)

li1 = copy.deepcopy(li)
li2 = copy.deepcopy(li)
li3 = copy.deepcopy(li)

shell_sort(li1)
#insert_sort(li2)
heap_sort(li3)
