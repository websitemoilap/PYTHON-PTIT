def th_nghich(n):
    return int(n) == int(str(n)[::-1])
t = int(input())
while t:
    n = int(input())
    sum1 = 0
    while n > 0:
        sum1 += (n%10)
        n //= 10
    if len(str(sum1)) > 1 and th_nghich(sum1):
        print("YES")
    else:
        print("NO")
    t -= 1