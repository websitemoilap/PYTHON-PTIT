from math import *
t = int(input())
def snt(n):
    cnt = 0
    if n < 2:
        return False
    else:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
while t:
    a, b = map(int, input().split())
    c = gcd(a, b)
    sum1 = 0
    while c > 0:
        k = c % 10
        sum1 += k
        c //= 10
    if snt(sum1):
        print("YES")
    else:
        print("NO")
    t-=1