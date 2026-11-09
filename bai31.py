#Bài 1: Viết hàm tìm giá trị lớn nhất trong 3 số
def max3so(a, b, c):
    """Trả về giá trị lớn nhất trong 3 số a, b, c"""
    return max(a, b, c)

# Ví dụ sử dụng:
print("Số lớn nhất trong 3, 9, 5 là:", max3so(3, 9, 5))