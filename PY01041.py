t = int(input())
while t > 0:
    n = input()
    if len(n) < 3:
        print("NO")
    else:
        max_digit = max(n)
        peak_index = n.index(max_digit)
        is_increasing = True
        for i in range(peak_index):
            if n[i] >= n[i+1]: 
                is_increasing = False
                break
        is_decreasing = True
        for i in range(peak_index, len(n)-1):
            if n[i] <= n[i+1]: 
                is_decreasing = False
                break
        if is_increasing and is_decreasing:
            print("YES")
        else:
            print("NO")

    t -= 1
