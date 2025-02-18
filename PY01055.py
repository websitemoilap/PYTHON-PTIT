def dk1(n):
    if len(n) % 2 != 0:
        return True
    else:
        return False
def dk2(n):
    return n[0] != n[1]
def dk3(n):
    for i in range(0, len(n)-2):
        return n[i] == n[i+2]
def check(n):
    return dk1(n) and dk2(n) and dk3(n)
t = int(input())
while t:
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")
    t -= 1