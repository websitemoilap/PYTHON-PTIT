t = int(input())
while t:
    s = input()
    ok = True
    for i in range(1, len(s)-1):
        if(s[i] > s[i+1]):
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")
    t -= 1