t = int(input())
while t:
    n = input()
    ok = True
    for i in range(0, len(n)-2, 1):
        while int(n[i]) != int(n[i+2]):
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")
    t -= 1
            
