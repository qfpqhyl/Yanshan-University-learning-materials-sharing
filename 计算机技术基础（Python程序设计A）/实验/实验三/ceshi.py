import math

def isPrime(num):
    flag = False
    if num >1:
        if num == 2:
            flag = True
        elif num%2 ==0:
            pass
        else:
            for i in range(3,num+1,2):
                if num%i ==0:
                    flag = True
    return flag


print(isPrime(321))