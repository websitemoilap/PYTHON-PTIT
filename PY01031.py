def dcs(n, b):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while n > 0:
        k = n % b
        res = digits[k] + res
        n //= b
    return res
t = int(input())
while t:
    n, b = list(map(int, input().split()))
    print(dcs(n, b))
    t -= 1