from math import *
def snt(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
t = int(input())
while t:
    n = int(input())
    print("1", end="")
    cnt = 0
    for i in range(2, int(sqrt(n))+1):
        if snt(i):
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            if cnt > 0:
                print(f" * {i}^{cnt}",end="")
    if n > 1:
        print(f" * {n}^1", end="")
    print()
    t -= 1