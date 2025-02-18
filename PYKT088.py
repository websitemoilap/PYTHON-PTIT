def check(n):
    cnt = 0
    cnt1 = 0
    for i in range(n+1):
        for k in range (1, i):
            if i % k == 0:
                cnt += 1
        if cnt == 9:
            cnt1 += 1
    return(cnt1)
n = int(input())
print(check(n))