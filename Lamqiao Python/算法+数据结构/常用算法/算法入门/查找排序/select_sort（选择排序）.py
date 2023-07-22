# _*_coding:utf-8_*_
# created by Alex Li on 11/5/17

def select_sort_simple(li):
    li_new = []
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new


def select_sort(li):
    for i in range(len(li)-1): # i是第几趟
        min_loc = i
        for j in range(i+1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]
        print(li)

li = [3,4,2,1,5,6,8,7,9]
print(li)
select_sort(li)
#print(li)