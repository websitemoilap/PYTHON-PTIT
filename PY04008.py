import sys

input_data = sys.stdin.read().strip().splitlines()
t = int(input_data[0])
index = 1

for _ in range(t):
    n, m = map(int, input_data[index].split())
    index += 1

    matrix = []
    
    for i in range(n):
        a = list(map(int, input_data[index].split()))
        matrix.append(a)
        index += 1
    
    ans = []
    
    for i in range(n):
        r = []
        for j in range(n):
            x = 0
            for k in range(m):
                x += matrix[i][k] * matrix[j][k]
            r.append(str(x))
        ans.append(r)
    
    for i in ans:
        print(" ".join(i))
