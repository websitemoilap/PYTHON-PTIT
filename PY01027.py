def check(n):
    cnt = 0
    for i in n:
        if i != '6' and i!= '8':
            return "NO"
        if i == '8': cnt += 1
        else: cnt = 0
        if cnt == 3: return "NO"
    return "YES"
n = input()
print(check(n))