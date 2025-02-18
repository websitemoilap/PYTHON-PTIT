def min_triple(arr):
    min1 = min2 = min3 = float('inf')
    for num in arr:
        if num < min1:
            min3 = min2
            min2 = min1
            min1 = num
        elif num < min2:
            min3 = min2
            min2 = num
        elif num < min3:
            min3 = num
    return min1 + min2 + min3
for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = min_triple(a)
    print(b)