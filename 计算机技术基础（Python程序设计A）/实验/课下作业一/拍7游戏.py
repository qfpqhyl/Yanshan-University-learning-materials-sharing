a = eval(input())

for i in range(1,a+1):
    if i%7 == 0:
        print(i)
    else:
        for j in str(i):
            if j == "7":
                print(i)