# a, k, n = map(int, input().split())
# res = []
# for b in range(1, n+1):
#     if (b <= n - a) and ((a + b) % k) == 0:
#         res.append(b)
# if not res:
#     print("-1")
# else:
#     res.sort()
#     print(*res)
# # dùng *phần tử để in cách
a , K , N = map(int,input().split())
#cong thuc tim so b dau tien
b = (K - ( a % K )) % K
check = False
for i in range(b, N - a + 1, K):
    if (i > 0):
        check = True
        print(i, end = " ")
if check == False: 
    print(-1)
