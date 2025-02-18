chuc_mung = set()
n = int(input())
for _ in range(n):
    s = input().strip()
    chuc_mung.add(s)
print(len(chuc_mung))
# Khi bạn sử dụng _, điều đó có thể giúp người đọc mã hiểu rằng bạn không cần đến giá trị 
# của biến trong vòng lặp và bạn chỉ muốn lặp qua một số lượng xác định.