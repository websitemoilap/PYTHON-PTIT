import sys
t = int(input())
hocsinh = []
while t:
    name = sys.stdin.read().strip()
    c, t = map(int, input().strip().split())
    hocsinh.append((name, c, t))
    t -= 1
hocsinh.sort(key=lambda x: (-x[1], x[2], x[0]))
for i in hocsinh:
    print(i[0], i[1], i[2])