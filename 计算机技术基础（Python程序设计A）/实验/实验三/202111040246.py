from random import random
import math
from turtle import *

def drawpi(DARTS):
    # 图形区域布局
    tracer(False)
    setup(400, 400,600,200)
    penup()
    goto(-150,-150)
    pensize(2)
    pencolor("black")
    pendown()
    for i in range(4):
        forward(300)
        left(90)
    penup()
    goto(-150,150)
    pendown()
    circle(-300,90)
    # 点的分布
    hits = 0.0
    for i in range(1,DARTS+1):
        x,y = random(),random()
        dist = math.sqrt(x**2 + y**2)
        if dist <= 1.0:
            hits += 1
            penup()
            goto(-150+300*x,-150+300*y)
            pendown()
            dot(3,"red")
        else:
            penup()
            goto(-150+300*x,-150+300*y)
            pendown()
            dot(3,"blue")
    tracer(True)
    pi = 4 * (hits/DARTS)
    print("Pi的值是{}".format(pi))
    done()

def isPrime(num):
    flag = True
    if num >1:
        if num == 2:
            flag = True
        elif num%2 ==0:
            flag = False
        else:
            for i in range(3,num,2):
                if num%i ==0:
                    flag = False
    return flag


if __name__ == "__main__":
    maxPrime = 0
    min = 1
    max = 5000
    for j in range(max,min-1,-1):
        flag = isPrime(j)
        if flag:
            maxPrime = j
            break
    print("{}~{}中最大的素数为{}".format(min,max,maxPrime))
    drawpi(maxPrime)