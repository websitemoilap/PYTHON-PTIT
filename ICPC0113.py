from math import sqrt
def sodao(n):
    reverse = 0
    while n != 0:
        reverse = reverse*10 + n % 10
        n //= 10
    return reverse
def snt(n):
    n = int(n)  
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
t = int(input())
while t > 0:
    n = input()
    for i in range(13, int(n)):
        dao = sodao(i)
        if snt(i) and snt(dao) and i != dao and i < dao:
            if i < int(n) and dao < int(n):
                print(i, dao, end=" ")
    print()
    t -= 1
