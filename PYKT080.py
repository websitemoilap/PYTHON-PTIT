m, n = map(int, input().split())
matrix = []
for _ in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

total_risk_cases = 0

# Define the 8 possible directions around a cell
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for i in range(m):
    for j in range(n):
        if matrix[i][j] == -1:
            for direction in directions:
                ni, nj = i + direction[0], j + direction[1]
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] >= 0:
                    total_risk_cases += matrix[ni][nj]

print(total_risk_cases)
