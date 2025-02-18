while True:
    x = input().strip()
    if x == '-1':
        break
    n = int(x)
    if n % 11 == 0:
        print('YES')
    else:
        print('NO')
