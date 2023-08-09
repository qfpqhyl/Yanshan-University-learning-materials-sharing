from math import *

a = input()
b = input()
c = input()
a = eval(a)
b = eval(b)
c = eval(c)
m, n = 0, 0


if a == 0:
    if b == 0:
        print("Data error")
    else:
        m = -c/b
        print("{}".format(m))
elif pow(b, 2)-4*a*c < 0:
    print("该方程无实数解")
elif pow(b, 2)-4*a*c == 0:
    m = -(b/a)*0.5
    print("{}".format(m))
elif pow(b, 2)-4*a*c > 0:
    m = (-b+sqrt(pow(b, 2)-4*a*c))/(2*a)
    n = (-b-sqrt(pow(b, 2)-4*a*c))/(2*a)
    if m > n:
        print("{}&{}".format(m, n))
    else:
        print("{}&{}".format(n, m))