# _*_coding:utf-8_*_
# created by Alex Li on 12/3/17

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

def merge(li, low, mid, high):
    i = low
    j = mid + 1
    ltmp = []
    while i<=mid and j<=high: # 只要左右两边都有数
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    # while执行完，肯定有一部分没数了
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1
    li[low:high+1] = ltmp


def _merge_sort(li, low, high):
    if low < high: #至少有两个元素，递归
        mid = (low + high) //2
        _merge_sort(li, low, mid)
        _merge_sort(li, mid+1, high)
        merge(li, low, mid, high)

@cal_time
def merge_sort(li):
    return _merge_sort(li, 0, len(li)-1)

import random,copy

li = list(range(100000))
random.shuffle(li)

li1 = copy.deepcopy(li)
li2 = copy.deepcopy(li)
li3 = copy.deepcopy(li)

quick_sort(li1)
heap_sort(li2)
merge_sort(li3)
