# n,m = 30,50
# see = set()  # 记录走过的点
# nums = [[int(x) for x  in input()] for _ in range(n)]
# def stop(x,y):
#   if x < 0 or y < 0 or x >= 30 or y >= 50 or nums[x][y] == 1 or ((x,y) in see):
#     return False
#   return True
# def bfs(x,y):
#   que = [(x,y,'')]
#   while que:
#     x,y,z = que.pop(0)
#     if stop(x,y):  # x,y没有超界
#       see.add((x,y))
#       que.append((x+1,y,z + 'D'))  # 按字母顺序，这样最后的出来的是顺序小的
#       que.append((x,y-1,z + 'L'))
#       que.append((x,y+1,z + 'R'))
#       que.append((x-1,y,z + 'U'))
#     if x == 29 and y == 49:
#       return z
# print(bfs(0,0))


# num = [1,1,1]
# for i in range(40):
#   num.append(num[-1] + num[-2] + num[-3])
# print(num[-1] % 1000000007)

# a, b, c, d = 1, 1, 1, 0
# for i in range(4, 20190325):
#     d = (a + b + c) % 10000
#     a, b, c = b, c, d
# print(a, b, c, d)

# 如果一个分数的分子和分母的最大公约数是1，这个分数称为既约分数。
# import math
# num = 0
# for i in range(1,2021):
#     for j in range(1,2021):
#         if math.gcd(i, j) == 1:
#             num += 1  # 既约分数的个数
# print(num)
# n = input()
# num = 0
# for i in range(1, int(n)+1):
#     if  "2" in str(i) or "0" in str(i) or "1" in str(i) or "9" in str(i):
#         num += i
# print(num)

# a,b,n = map(int,input().split())
# num = 0
# date = 0

# for i in range(5):
#     num += a
#     date += 1
#     if num >= n:
#       print(date)
#       break
        
# #   for i in range(2):
# #       num += b
# #       date += 1
# #       if num >= n:
# #           print(date)
# #           break
# #   date += 7

# num = 0
# i =0
# a,b,n=list(map(int,input().split()))
# while True:
#   i+=1
#   if i%7 in [1,2,3,4,5]:
#     num+=a
#   elif i%7 in [0,6]:
#     num+=b
#   if num >= n:
#     break
# print(i)


# a = 2019%26  #个位
# b = 2019//26 
# c = b%26     #十位
# d = b//26    #百位
# list = '*ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# print(list[d]+list[c]+list[a])
# import math
# print(math.comb(5,2))


# sum =set()
# n = int(input())
# num = [int(x) for x in input().split()]
# sum.add(0)
# for i in num:
#     for j in list(sum):
#         sum.add(i+j)
#         sum.add(abs(i-j))
# print(len(sum)-1)
# import math
# ans = []
# n = int(input())
# num = [int(x) for x in input().split()]
# for i in range(n):
#     for j in range(i+1,n):
#         ans.append(num[i]*num[j])
# print(sum(ans))
# n=int(input())


# S=0
# a=list(map(int,input().split()))
# s1=sum(a)
# for i in range(0,n):
#     s1-=a[i]
#     S+=a[i]*s1
# print(S)
# n = int(input())
# num = [[int(x) for x in input().split()] for _ in range(n)]
# for i in range(1,n):
#     for j in range(i+1):
#         if j == 0:
#             num[i][j] += num[i-1][j]
#         elif j == i:
#             num[i][j] += num[i-1][j-1]
#         else:
#             num[i][j] += max(num[i-1][j-1], num[i-1][j])
# if n%2 == 1:
#     print(num[-1][n//2])
# else:
#     print(max(num[-1][n//2], num[-1][n//2-1]))
# 数学老师给小明出了一道等差数列求和的题目。但是粗心的小明忘记了一 部分的数列，只记得其中N个整数。
# 现在给出这 N 个整数，小明想知道包含这 N 个整数的最短的等差数列有几项？
# n = int(input())
# num = [int(x) for x in input().split()]

# minnum = min(num)
# maxnum = max(num)
# for i in range(1,n):
#     if minnum + i in num:
#         print(int((maxnum - minnum)/i) + 1)
#         break

# n = int(input())
# num = [int(x) for x in input().split()]
# num = sorted(num)
# for i in range(n-1):
#     tem = num[i+1]-num[i]
#     if i == 0:
#         ans = tem
#     else:
#         ans = min(ans,tem)
# if ans == 0:
#     print(n)
# else:
#     print(int((num[-1]-num[0])/ans) + 1)

# 乐羊羊饮料厂正在举办一次促销优惠活动。乐羊羊 C 型饮料，凭 3 个瓶盖可以再换一瓶 C 型饮料，并且可以一直循环下去(但不允许暂借或赊账)。
# 请你计算一下，如果小明不浪费瓶盖，尽量地参加活动，那么，对于他初始买入的 n 瓶饮料，最后他一共能喝到多少瓶饮料。
# n = int(input())
# num = 0
# if n < 3:
#     print(n)
# else:    
#     while n >= 3:
#         num += (n-n%3)
#         n = n//3 + n%3
#     print(num+n)


# 请在此输入您的代码
# n,m=map(int,input().split())
# M=-999
# def dfs(x,y,v):
#   if(x==n-1 and y==m-1):
#     global M
#     M=max(M,v)
#     return 0
  
#   if x+1<n:
#     dfs(x+1,y,v+road[x+1][y])
#   if x+2<n:
#     dfs(x+2,y,v+road[x+2][y])
#   if x+3<n:
#     dfs(x+3,y,v+road[x+3][y])
#   if y+1<m:
#     dfs(x,y+1,v+road[x][y+1])
#   if y+2<m:
#     dfs(x,y+2,v+road[x][y+2])
#   if y+3<m:
#     dfs(x,y+3,v+road[x][y+3])
#   if x+1<n and y+1<m:
#     dfs(x+1,y+1,v+road[x+1][y+1])
#   if x+1<n and y+2<m:
#     dfs(x+1,y+2,v+road[x+1][y+2])
#   if x+2<n and y+1<m:
#     dfs(x+2,y+1,v+road[x+2][y+1])

# road=[]
# for i in range(n):
#   road.append(list(map(int,input().split())))
# dfs(0,0,road[0][0])
# print(M)

# import datetime
# date = datetime.date(1950,1,1)
# for i in range(100):
#     date = date + datetime.timedelta(days=1)
#     if int(date.strftime("%Y%m%d"))%2012 == 0 and int(date.strftime("%Y%m%d"))%3 == 0 and int(date.strftime("%Y%m%d"))%12 == 0:
#         print(date.strftime("%Y%m%d"))
#         break
# print(("%02d%02d%02d") %(date.year,date.month,date.day))
# # print(date.strftime("%Y%m%d"))
# print(int(str(date).replace('-','')))

# for i in range(1950,1960):
#     for j in range(1,31):
#         print(str(int(str(i)+str('06')+str("%02d" %j))/2012*3*12) + "日期"+ str(i)+str('06')+str("%02d" %j))
# daice = "WHERETHEREISAWILLTHEREISAWAY"
# num = []
# zimu = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
# for i in zimu:
#     num.append(i*daice.count(i))
# print(num)