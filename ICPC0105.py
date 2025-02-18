for t in range(int(input())):
    s = input()
    num = []
    sht = ""
    for i in s:
        if i.isdigit():
            sht += i
        else:
            if sht:
                num.append(sht)
                sht = ""
    if sht:
        num.append(sht)
    number = list(map(int, num))
    if number:
        sln = max(number)
        print(sln)