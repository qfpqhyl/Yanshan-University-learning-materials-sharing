import pandas as pd
import numpy as np
import math
import time
 
dataframe = pd.read_csv("城市信息表.csv",header=None)
v = dataframe.iloc[:,1:3]
 
train_v= np.array(v)
train_d=train_v
dist = np.zeros((train_v.shape[0],train_d.shape[0]))
 
#计算距离矩阵
for i in range(train_v.shape[0]):
    for j in range(train_d.shape[0]):
        dist[i,j] = math.sqrt(np.sum((train_v[i,:]-train_d[j,:])**2))
"""
s:已经遍历过的城市
dist：城市间距离矩阵
sumpath:目前的最小路径总长度
Dtemp：当前最小距离
flag：访问标记
"""
i=1
n=train_v.shape[0]
j=0
sumpath=0
s=[]
s.append(0)
start=time.clock()
while True:
    k=1
    Detemp=10000000
    while True:
        l=0
        flag=0
        if k in s:
            flag=1
        if (flag==0)and(dist[k][s[i-1]]<Detemp):
            j=k;
            Detemp=dist[k][s[i-1]];
        k+=1
        if k>=n:
            break;
    s.append(j)
    i+=1;
    sumpath+=Detemp
    if i>=n:
        break;
sumpath+=dist[0][j]
end=time.clock()
print("结果：")
print(sumpath)
for m in range(n):
    print("%s->"%(s[m]),end='')
print()