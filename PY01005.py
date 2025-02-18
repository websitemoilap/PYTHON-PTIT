t = int(input())
while t:
    n = str(input())
    cnt = 0
    for i in n:
        if i == '4' or i == '7':
            cnt += 1
    if cnt != 0 and len(n) == cnt:
        print("YES")
    else:
        print("NO")
    t -= 1
        