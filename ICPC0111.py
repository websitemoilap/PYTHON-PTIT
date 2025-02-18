t = int(input())
while t:
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    x1 = a[d:]
    x2 = a[:d]
    res = x1 + x2
    print(*res)
    t -= 1