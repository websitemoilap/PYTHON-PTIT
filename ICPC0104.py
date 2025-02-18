for t in range(int(input())):
    s = input()
    res = ""
    num = []
    for i in s:
        if i.isdigit():
            res += i
        else:
            if res:
                num.append(res)
                res = ""
    if res:
        num.append(res)
    number = list(map(int, num))
    if number:
        sbn = min(number)
        print(sbn)