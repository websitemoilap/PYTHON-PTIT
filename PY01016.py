t = int(input())
while t:
    s = input().strip()
    res = []
    i = 0
    while i < len(s):
        char = s[i]
        i += 1
        count = int(s[i])
        i += 1
        res.append(char * count)
    print("".join(res))
    t -= 1
# join sử dụng để nối các từ thành 1 chuỗi duy nhất3