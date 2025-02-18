for _ in range(int(input())):
    n = input()
    sum_digit = 0
    prod_digit = 1
    allzero = True
    for i in range(0,len(n)):
        if i % 2 == 0:
            sum_digit = sum_digit +  int(n[i])
        elif i % 2 != 0:
            if (n[i] != "0"):
                allzero = False
                prod_digit *= int(n[i])
    if allzero:
        print(sum_digit," ","0")
    else:
        print(sum_digit," ",prod_digit)