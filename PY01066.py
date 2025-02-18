t = int(input())
while t:
    n = input()
    n1 = n[::-1]
    ok = True
    for i in range(len(n)):
        if abs(ord(n[i])-ord(n[i-1])) != abs(ord(n1[i])-ord(n1[i-1])):
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")
    t -= 1