def Convert(n):
    if n >= 3 and n <= 4: return 2.5
    if n >= 5 and n <= 6: return 3.0
    if n >= 7 and n <= 9: return 3.5
    if n >= 10 and n <= 12: return 4.0
    if n >= 13 and n <= 15: return 4.5
    if n >= 16 and n <= 19: return 5.0
    if n >= 20 and n <= 22: return 5.5
    if n >= 23 and n <= 26: return 6.0
    if n >= 27 and n <= 29: return 6.5
    if n >= 30 and n <= 32: return 7.0
    if n >= 33 and n <= 34: return 7.5
    if n >= 35 and n <= 36: return 8.0
    if n >= 37 and n <= 38: return 8.5
    if n >= 39 and n <= 40: return 9.0
for t in range(int(input())):
    r, l, s, w = map(float, input().split())
    read_score = Convert(r)
    listen_score = Convert(l)
    overall = (read_score + listen_score + s + w) / 4
    phandu = overall % 1.0
    if phandu < 0.25:
        overall = int(overall) + 0.0
    elif phandu >= 0.25 and phandu < 0.75:
        overall = int(overall) + 0.5 
    else:
        overall = int(overall) + 1.0
    print(overall)   