n = int(input())
res = list(map(int, input().split()))
cnt = 0
for i in range(0, len(res)-1):
    if res[i] != res[i+1]:
        cnt += 1
print(cnt)