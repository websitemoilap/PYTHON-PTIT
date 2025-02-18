from math import *
def snt(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
t = int(input())
while t:
    n = int(input())
    cnt = 0
    for i in range(1, n):
        b = gcd(i, n)
        if(b == 1):
            cnt += 1
    if snt(cnt):
        print("YES")
    else:
        print("NO")
    t -= 1