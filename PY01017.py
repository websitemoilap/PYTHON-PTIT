t = int(input())
while t:
    s = str(input())
    cnt = 1
    result  = ""
    for i in range(1, len(s)):
        if (s[i] == s[i-1]):
            cnt += 1
        else:
            result += str(cnt) + s[i-1]
            cnt = 1
    result += str(cnt) + s[-1]
    print(result)
    t-= 1