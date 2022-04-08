from random import *
from math import *
n = int(input("Enter any number: "))
s = {(randint(-100, 100) , randint(-100, 100)) for i in range(n) }
print(s)
mindist=inf
optimalp=(None,None)
for p in s :
    for q in s-{p}:
        d=sqrt((p[0]-q[0])**2+(p[1]-p[1])**2)
        print(d)
        if d<mindist:
            mindist=d
            optimalp=(p,q)
print(optimalp,mindist)