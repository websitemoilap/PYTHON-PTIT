t = int(input())
while t:
    n = int(input())
    tich = 1
    while n > 0 and len(str(n)) <= 500:
        k = n % 10
        if k != 0:
            tich *= k
        else:
            tich += 0
        n //= 10
    print(tich)