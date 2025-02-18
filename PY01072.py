import itertools
n , k = map(int, input().split())
a = list(map(int, input().split()))
if len(a) == n:
    b = sorted(set(a))
    to_hop = itertools.combinations(b, k)
    for i in to_hop:
        print(i)

# combinations : tổ hợp