def check(a):
    n = len(a)
    ds = set()
    res = []
    for i in range(0, n-1, 2):
        num = int(a[i:i+2])
        if num not in ds:
            ds.add(num)
            res.append(num)
    return " ".join(map(str, sorted(res)))
n = input().strip()
print(check(n))
