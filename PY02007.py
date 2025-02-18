import sys
a = list(map(int, sys.stdin.read().split()))
res = []
ok = True
if len(a) == 10:
    for i in range(len(a)):
        k = a[i] % 42
        res.append(k)
    b = set(res)
    print(len(b))

