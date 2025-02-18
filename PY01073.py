import itertools
s = str(input())
hoan_vi = itertools.permutations(s)
for i in hoan_vi:
    print("".join(i))
# permutations : hoán vị