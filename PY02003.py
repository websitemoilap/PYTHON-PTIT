from math import sqrt

def snt(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def check(n):
    if n == 1:
        return True  # 1 thỏa mãn điều kiện
    res = set()
    
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            res.add(i)
            res.add(n // i)  # Lấy cả cặp ước số
        
    if all(x <= 5 for x in res):
        return True
    return False

t = int(input())  
while t > 0:
    t -= 1  # Giảm biến đếm t để tránh vòng lặp vô hạn
    n = int(input())
    cnt = 0
    for i in range(1, n + 1):  # Kiểm tra từng số từ 1 đến n
        if check(i):  
            cnt += 1
    print(cnt)
