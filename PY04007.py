import sys
for t in range(int(input())):
    n, m =map(int, input().split())
    matrix = []
    for i in range(n):
        a = list(map(int, sys.stdin.read().split()))
        matrix.append(a)
    ans = []
    for i in range(n):
        r = []
        for j in range(n):
            x = 0
            for k in range(m):
                x += matrix[i][k] * matrix[j][k]
            r.append(str(x)) # kết quả nằm trên một hàng
        ans.append(r) # kết quả của ma trận
    for i in ans:
        print(" ".join(i))