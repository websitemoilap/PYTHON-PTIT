import sys
n = int(input())
a = list(map(int, sys.stdin.read().split()))
sochan = sorted([x for x in a if x % 2 == 0])
sole = sorted([x for x in a if x % 2 == 1], reverse=True)
res = []
index1, index2 = 0, 0
for num in a:
    if num % 2 == 0:
        res.append(sochan[index1])
        index1 += 1
    else:
        res.append(sole[index2])
        index2 += 1
print(*res)