t = int(input())
while t:
    n = input().strip()
    sum1 = sum(int(digit) for digit in n)
    ok = False
    if sum1 % 10 == 0:
        for i in range(len(n)-1):
            if abs(int(n[i]) - int(n[i+1])) == 2:
                ok = True
                break
    else:
        ok = False
    if ok:
        print("YES")
    else:
        print("NO")
    t -= 1

