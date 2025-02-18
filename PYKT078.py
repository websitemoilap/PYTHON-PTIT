for t in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    max_value = max(a)
    max_index = a.index(max_value)
    a.insert(max_index, k)
    am = [x for x in a if x < 0]
    duong = [x for x in a if x >= 0]
    result = am + duong
    print(*result)