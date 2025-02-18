def sodao(n):
    return int(str(n)[::-1])
t = int(input())
while t:
    n = int(input())
    sum = 0
    ok = False
    for _ in range(1000):
        if n % 7 == 0:
            print(n)
            ok = True
            break
        n = n + sodao(n)
    if not ok:
        print("-1")
    t -= 1