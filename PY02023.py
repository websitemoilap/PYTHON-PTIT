from math import *
t = int(input())
while t:
    n = int(input())
    a = list(map(int, input().split()))
    pairs = []
    for num in a:
        tich_so = prod(int(digit) for digit in str(num))
        pairs.append((tich_so, num))
    pairs.sort()
    result = [pair[1] for pair in pairs]
    print(*result)
    t -= 1