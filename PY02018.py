n = int(input())
a = list(map(int, input().split()))
res = 1
a.sort()
for i in a:
    if i > res:
        break
    elif i == res:
        res += 1        
print(res)
