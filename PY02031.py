from math import *
def check(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
n, m = map(int, input().split())
matrix = []
for i in range(n):
    a = list(map(int, input().split()))
    matrix.append(a)
for i in range(n):
    for j in range(m):
        if check(matrix[i][j]):
            matrix[i][j] = 1
        else:
            matrix[i][j] = 0
for i in matrix:
    print(*i)