#Bài 3: Viết hàm tìm bội chung nhỏ nhất (BCNN) của 2 số a và b
import math

def tim_bcnn(a, b):
    """Tìm BCNN của a và b sử dụng ước chung lớn nhất (GCD)"""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // math.gcd(a, b)

# Ví dụ sử dụng:
print("BCNN của 4 và 6 là:", tim_bcnn(4, 6))