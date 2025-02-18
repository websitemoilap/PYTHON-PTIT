t = int(input())
while t:
    s = str(input())
    if len(s) >= 2 and s[-2:] == '86':
        print("YES")
    else:
        print("NO")
    t -= 1