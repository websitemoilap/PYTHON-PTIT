import sys
n = int(input())
a = list(map(int, sys.stdin.read().split()))
res = []
for i in range(1, n+1):
    if i not in a:
        res.append(i)
if len(res) == 0:
    print("Excellent!")
else:
    for num in res:
        print(num, end="\n")