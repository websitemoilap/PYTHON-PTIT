def dem(a, b):
    return a.count(b)
t = int(input())
while t:
    a = input()
    b = input()
    print(dem(a, b))
    t -= 1