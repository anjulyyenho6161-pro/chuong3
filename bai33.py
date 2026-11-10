#Bài 3: Viết hàm tìm bội chung nhỏ nhất (BCNN) của 2 số a và b
import math
# Viết hàm tìm bội chung nhỏ nhất (BCNN) sử dụng ước chung lớn nhất (UCLN)
def BCNN(a, b):#a = int(input("Nhập số thứ nhất (a): "))
    if a == 0 or b == 0:#b = int(input("Nhập số thứ hai (b): "))
        return 0
    # Công thức: BCNN(a, b) = (|a * b|) / UCLN(a, b)
    ucln = math.gcd(a, b)
    bcnn = abs(a * b) // ucln
    return bcnn
print(f"Bội chung nhỏ nhất: ",BCNN(5,10))
'''def timbcnn(a, b):
    bc = max(a, b)
    while bc % a or bc % b: bc += max(a, b)
    return bc

print("bội chung nhỏ nhất của 2 số a, b là:", timbcnn(4, 6))
def ucln_de_quy(a, b):
    if b == 0:
        return a
    return ucln_de_quy(b, a % b)
