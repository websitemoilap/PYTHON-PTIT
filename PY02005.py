n = int(input())
res = list(map(int, input().split()))
cnt  = 0
for i in range(0, n):
    for j in range(i + 1, n):
        if res[i] > res[j]:
            cnt += 1
print(cnt)

