s1 = input().split()
s2 = input().split()
u, v = set(), set()
for i in s1:
    u.add(i.lower())
    for j in s2:
        if i.lower() == j.lower():
            v.add(i.lower())
for i in s2:
    u.add(i.lower())
print(" ".join(sorted(u)))
print(" ".join(sorted(v)))