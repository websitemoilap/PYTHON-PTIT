def check(n):
    sum = 0
    for i in n:
        sum += ord(i) - ord('0')
    return str(sum)
n = input()
cnt = 0
while len(n) > 1:
    n = check(n)
    cnt += 1
print(cnt)