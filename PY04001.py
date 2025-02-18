from math import sqrt
t = int(input())
while t:
    x1, y1, x2, y2 = map(int, input().split())
    print(round(sqrt((x2 - x1)**2 + (y2 - y1)**2), 4))