for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    max_value = max(a)
    min_value = min(a)
    res = []
    for i in range(min(a), max(a) + 1):
        if i not in a:
            res.append(i)
    print(len(res))