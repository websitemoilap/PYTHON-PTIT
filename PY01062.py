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
    n = input()
    cnt = 0
    cnt1 = 0
    for i in range(len(n)):
        if snt(int(n[i])):
            cnt += 1
        else:
            cnt1 += 1
    if snt(len(n)) and cnt > cnt1: 
        print("YES")
    else:
        print("NO")
    t -= 1