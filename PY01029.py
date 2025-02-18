from math import *
t = int(input())
while t:
    s = input().strip()
    b = gcd(int(s), int(s[::-1]))
    if (b == 1):
        print("YES")
    else:
        print("NO")
    t -= 1