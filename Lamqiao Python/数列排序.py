n = int(input())
list = input().split()
lists = []
for i in list:
    lists.append(int(i))
lists.sort()
for j in lists:
    print(j,end = " ")