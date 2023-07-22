def hannoi(n,a,b,c):
    if n > 0:
        hannoi(n-1,a,c,b)
        print("moving from %s to %s" %(a,c))
        hannoi(n-1,b,a,c)
hannoi(30,'a','b','c')