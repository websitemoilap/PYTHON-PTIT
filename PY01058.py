from math import sqrt
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
t = int(input())
while t:
    n = int(input())
    if is_prime(int(str(n)[-4:])):
        print("YES")
    else:
        print("NO")
    t -= 1