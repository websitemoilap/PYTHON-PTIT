from math import *
def snt(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True
t = int(input())
while t:
    n = int(input())
    sum1 = 0
    while n > 0:
        sum1 += (n%10)
        n //= 10
    if snt(sum1): print("YES")
    else:
        print("NO")
    t -= 1