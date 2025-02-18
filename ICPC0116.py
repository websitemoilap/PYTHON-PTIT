# t = int(input())
# while t:
#     n = int(input())
#     res = []
#     while(n > 0):
#         k = n % 10
#         res.append(k)
#         n //= 10
#     if res[0] == res[-1]:
#         print("YES")
#     else:
#         print("NO")
#     t -= 1
t = int(input())
while t:
    s = str(input())
    if s[0] == s[len(s)-1]:
        print("YES")
    else:
        print("NO")
    t -= 1