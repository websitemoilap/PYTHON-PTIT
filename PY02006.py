t = int(input())
while t:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    sxa = sorted(a)
    sxb = sorted(b)
    ok = True
    for i in range(n):
            if sxa[i] > sxb[i]:
                ok = False
                break
    if ok:
        print("YES")
    else:
        print("NO")
    t -= 1
