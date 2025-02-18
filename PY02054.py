n, m = map(int, input().split())
matrix = []
for i in range(n):
    a = list(map(int, input().split()))
    matrix.append(a)
for i in range(n):
    for j in range(m):
        if n > m:
            if i % 2 == 0:
                print(matrix[i][j])
        elif n < m:
            if i % 2 == 1:
                print(matrix[i][j])
for i in range(n):
    for j in range(m):
        print(matrix[i][j])