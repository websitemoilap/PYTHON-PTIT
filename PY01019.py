t = int(input())
while t:
    s1 = input()
    s2 = s1[::-1]
    ok = False
    for i in range(1, len(s1)):
        if (abs(ord(s1[i]) - ord(s1[i-1])) != abs(ord(s2[i]) - ord(s2[i-1]))):
            ok = True
            break
    if ok:
        print("NO")
    else:
        print("YES")
    t-=1
# ord là đối số trả về mã unicode