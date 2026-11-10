#Bài 2: Viết hàm tính tổng $S = 1 + 2 + 3 + 4 + 5 ... + n
def tinhtong(n):
    s=0
    for i in range(1,n+1):
        s=s+i
    return s
print(tinhtong(5))
#cách 2 dùng quy nạp
def tong(n):
    return n*(n+1)/2
print(tong(5))
