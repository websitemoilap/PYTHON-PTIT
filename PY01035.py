def check(n):
    while len(n) % 3 != 0:
        n = "0" + n
    res = ""
    for i in range(0, len(n), 3):
        res += str(int(n[i:i+3], 2)) # trong python hàm int(n, hệ cơ số) là hàm chuyển hệ cơ số đó
    return res
n = input()
print(check(n))