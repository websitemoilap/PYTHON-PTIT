N = int(input())
A = list(map(int, input().split()))
A.sort()
max_product_1 = A[-1] * A[-2]
max_product_2 = A[-1] * A[-2] * A[-3]
max_product_3 = A[0] * A[1] * A[-1]
max_product = max(max_product_2, max_product_3, max_product_3)
print(max_product)
