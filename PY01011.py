def check(n):
    if len(str(n)) % 2 == 0:
        return True
    return False
def check1(n):
    while n > 0:
        k = n % 10
        if k in {0, 2, 4, 6, 8}:
            return True
        n //= 10
        return False
def check3(n):
    return int(str(n)) == int(str(n)[::-1]) and check1(n) and check(n)
t = int(input())
while t:
    n = int(input())
    for i in range(1, n):
        if check3(i):
            print(i, end="\t")
    t -= 1