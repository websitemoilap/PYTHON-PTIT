t = int(input())
while t:
    n = input()
    res = []
    sum1= 0
    for i in n:
        if i.isalpha():
            res.append(i)
        elif i.isnumeric():
            sum1 += int(i)
    res.sort()
    if sum1 > 0:
        print("".join(res) + str(sum1))
    else:
        print("".join(res) + "")
    t -= 1