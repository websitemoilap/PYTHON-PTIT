t = int(input())
while t:
    n = input()
    cnt = 0
    for i in range(len(n)):
        if n[i] == "0" or n[i] == "1" or n[i] == "2":
            cnt += 1
    if len(n) == cnt:
        print("YES")
    else:
        print("NO")
    t -= 1
    