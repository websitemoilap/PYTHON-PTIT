from math import *
def snt(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
n = int(input())
a = list(map(int, input().split()))
res1 = {}
res = []
for num in a:
    if snt(num):
        if num in res1:
            res1[num] += 1
        else:
            res1[num] = 1
            res.append(num)
for num in res:
    print(num, res1[num])
    