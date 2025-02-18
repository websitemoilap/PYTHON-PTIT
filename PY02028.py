from math import *
def snt(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
n = int(input())
a = list(map(int, input().split()))
prime_index = 0
primes = [num for num in a if snt(num)]
primes.sort()
for i in range(n):
    if snt(a[i]):
        a[i] = primes[prime_index]
        prime_index += 1
print(*a)