n = int(input())
a = list(map(float, input().split()))
a.sort()
sum = 0
cnt = 0
for i in range(0, n):
    if a[i] != a[0] and a[i] != a[-1]:
        sum += a[i]
        cnt += 1
b = sum / cnt 
print(round(b, 2))