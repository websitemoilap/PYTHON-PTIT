t = int(input())
while t:
    n = input()
    sum1 = 0
    tich = 1
    ok = True
    for i in range(0, len(n)):
        if i % 2 == 0:
            if n[i] != "0":
                ok = False
                tich *= int(n[i])
        else:
            sum1 += int(n[i])
    if ok:
        print(tich," ","0")
    else:
        print(tich," ",sum1)
    t -= 1