t = int(input())
while t:
    n, x, m = map(float, input().split())
    years = 0
    while n < m:
        n = n + n*(x/100)
        years += 1
    print(years)
    t -= 1