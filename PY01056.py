from math import *
def dk1(n):
    for i in range(len(n)):
        if (i % 2 == 0 and int(n[i]) % 2 != 0) or (i % 2 != 0 and int(n[i]) % 2 == 0):
            return False
    return True
def snt(n):
    if int(n) < 2: return False
    for i in range(2, int(sqrt(int(n)))+1):
        if int(n) % i == 0:
            return False
    return True
def dk2(n):
    sum1 = sum(int(digit) for digit in n) 
    return snt(sum1)
def check(n):
    return dk1(n) and dk2(n)
t = int(input())
while t:
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")
    t -= 1
        