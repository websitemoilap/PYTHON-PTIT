def gt(n):
    dp = [1]
    for i in range(1, 10):
        dp.append(dp[-1] * i)
t = int(input())        
while t:
    n = int(input())
    sum1 = 0
    tmp = n
    while n > 0:
        k = n% 10
        sum1 += gt(k)
        n //= 10
    if sum1 == tmp:
        print("YES")
    else:
        print("NO")
    t -= 1