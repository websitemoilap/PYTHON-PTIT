t = int(input())
while t:
    n = int(input())
    sum1 = 0
    if n % 2 == 1:
        for i in range(1, n + 1, 2):
            sum1 += (1/i)
    else:
        for i in range(2, n + 1, 2):
            sum1 += (1/i)
    print(f"{sum1:.6f}")
    t -= 1
# không dùng round được vì nó sẽ mất chính xác ở một số trường hợp như có 0 ở sau