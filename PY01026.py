t = int(input())
test = 1
while t:
    a = []
    b = []
    s1 = input()
    s2 = input()
    for i in s1:
        a.append(i)
    for i in s2:
        b.append(i)
    a.sort()
    b.sort()
    ok = True
    for i in range(len(a)):
        if a[i] != b[i] or len(a) != len(b):
            ok =False
            break
    if ok :
        print(f"Test {test}: YES")
    else:
        print(f"Test {test}: NO")
    test += 1
    t -= 1