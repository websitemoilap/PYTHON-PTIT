from math import *
n, k = map(int, input().split(" "))
res = []
for i in range(10**(k-1), 10**k - 1, 1):
    if gcd(n, i) == 1:
        res.append(i)
for i in range(0, len(res), 10):
    print(*res[i:i+10])