from collections import Counter
for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    counts = Counter(a)
    for i, j in counts.items():
        if j % 2 == 1:
            print(i)
            break