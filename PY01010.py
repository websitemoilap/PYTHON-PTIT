t = int(input())
while t:
    str = input()
    if (int(str[0]) == int(str[-2]) and int(str[1]) == int(str[-1])):
        print("YES")
    else:
        print("NO")
    t -= 1