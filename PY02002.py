f = [1] * 93
for i in range(3, 93):
    f[i] = f[i-1] + f[i-2]
t = int(input())
while t:
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        print(f[i], end=" ")
    print()
    t -= 1
