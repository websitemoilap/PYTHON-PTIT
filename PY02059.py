from math import sqrt
def snt(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
n, m = map(int, input().split())
matrix = []
ok = False  
for i in range(n):
    a = list(map(int, input().split()))
    matrix.append(a)
sntln = -1  
for i in range(n):
    for j in range(m):
        if snt(matrix[i][j]):
            if matrix[i][j] > sntln:
                sntln = matrix[i][j]  
if sntln == -1:
    print("NOT FOUND")
else:
    print(sntln)  
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == sntln:
                print(f"Vi tri [{i}][{j}]")
