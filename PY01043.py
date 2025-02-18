# def check(n):
#     if len(n) % 2 == 1 or n != n[::-1]:
#         return False
#     for i in n:
#         if int(i) % 2 == 1:
#             return False
#     return True
# t = int(input())
# while t:
#     n = int(input())
#     for i in range(22, n, 2):
#         if check(str(i)):
#             print(i, end=" ")
#     print()
#     t -= 1 
def check(n):
    for i in range(len(n)):
        if (int(n[i]) %2!=0) : return False
    return True
for i in range(int(input())):
    n = int(input())
    num =""
    for i in range(2,10000):
        num = str(i) + str(i)[::-1]
        if (check(num) and int(num) < n and len(num) %2 ==0):
           print(num, end =" ")
    print()
           
