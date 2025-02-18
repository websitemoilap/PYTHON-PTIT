from math import *
def snt(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
def check(n):
    sum = 0
    b = n
    while n > 0:
        k = n % 10
        if k not in {2, 3, 5, 7}:
            return False
        sum += k
        n //= 10
    return snt(b) and snt(int(str(b)[::-1])) and snt(sum)
t = int(input())
while t:
    n = int(input())
    if check(n):
        print("YES")
    else:
        print("NO")
    t -= 1 