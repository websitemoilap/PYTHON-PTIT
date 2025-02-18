n, m = map(int, input().split())
matrix = []
for i in range(n):
    a = list(map(int, input().split()))
    matrix.append(a)
gtln = -float('inf') # tạo ra một giá trị cực kì bé
gtnn = float('inf')  # tạo ra một giá trị rất lớn
for i in range(n):
    for j in range(m):
        gtln = max(gtln, matrix[i][j])
        gtnn = min(gtnn, matrix[i][j])
k = gtln - gtnn
ok = False
for i in range(n):
    for j in range(m):
        if matrix[i][j] == k:
            if not ok: 
                print(k)
                ok = True
            print(f"Vi tri [{i}][{j}]")
if not ok:
    print("NOT FOUND")