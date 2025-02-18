n = int(input())
matrix = []
for i in range(n):
    a = list(map(int, input().split()))
    matrix.append(a)
k = int(input())
sum1 = 0
sum2 = 0
for i in range(n):
    for j in range(n):
        if i + j < n - 1:
            sum1 += matrix[i][j]
        elif i + j > n - 1:
            sum2 += matrix[i][j]
c = abs(sum1 - sum2)
if c <= k:
    print("YES")
    print(c)
else:
    print("NO")
    print(c)