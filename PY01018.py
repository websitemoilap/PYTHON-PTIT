P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    line = input().strip()
    if line == "0":
        break
    k, s = line.split()
    k = int(k)
    res = []
    for char in s:
        old_index = P.index(char)
        new_index = (old_index + k) % 28
        res.append(P[new_index])
    res = "".join(res[::-1])
    print(res)