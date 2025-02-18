from math import sqrt
def check(n):
    if len(str(n)) >= 2:
        return int(str(n)) == int(str(n)[::-1])
    else:
        return False
n, m = map(int, input().split())
matrix = []
ok = False  
for i in range(n):
    a = list(map(int, input().split()))
    matrix.append(a)
sodaoln = -1  
for i in range(n):
    for j in range(m):
        if check(matrix[i][j]):
            if matrix[i][j] > sodaoln:
                sodaoln = matrix[i][j]  
if sodaoln == -1:
    print("NOT FOUND")
else:
    print(sodaoln)  
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == sodaoln:
                print(f"Vi tri [{i}][{j}]")
