from math import *
l, r = map(int, input().split(" "))
res = []
for a in range(l, r-1):
    for b in range(a+1, r):
        for c in range(b+1, r+1):
            if(gcd(a,b) == gcd(a,c) == gcd(b,c) == 1):
                res.append((a, b, c))
for i in res:
    print(i)