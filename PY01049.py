from math import sqrt

def snt(n):
    if n < 2: 
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def check(n):
    cnt = 0
    cnt1 = 0
    if len(n) < 3:
        return False
    else:
        for digit in n:
            if snt(int(digit)): 
                cnt += 1
            else:
                cnt1 += 1
    if (cnt > cnt1) and snt(len(n)):
        print("YES")
    else:
        print("NO")

t = int(input())
while t:
    n = input()  
    check(n)
    t -= 1
