for t in range(int(input())):
    m, n = map(int, input().split())
    x = [[0]]*m
    h = [[0]]*3
    for i in range(m):
        x[i] = list(map(int, input().split()))
    for i in range(3):
        h[i] = list(map(int, input().split()))
    matrix = []
    sum1 = 0
    for i in range(3):
        for j in range(3):
            matrix.append(h[i][j])
    for i in range(2, m):
        for j in range(2, n):
            sum1 += x[i-2][j-2] * h[0][0]
            sum1 += x[i-2][j-1] * h[0][1]
            sum1 += x[i-2][j] * h[0][2]
            sum1 += x[i-1][j-2] * h[1][0]
            sum1 += x[i-1][j-1] * h[1][1]
            sum1 += x[i-1][j] * h[1][2]
            sum1 += x[i][j-2] * h[2][0]
            sum1 += x[i][j-1] * h[2][1]
            sum1 += x[i][j] * h[2][2]
    print(sum1)