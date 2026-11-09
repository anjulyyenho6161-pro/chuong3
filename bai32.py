#Bài 2: Viết hàm tính tổng $S = 1 + 2 + 3 + 4 + 5 ... + n
def tongs(n):
    """Tính tổng từ 1 đến n"""
    s = sum(range(1, n + 1))
    return s

# Ví dụ sử dụng:
n = 5
print(f"Tổng S từ 1 đến {n} là:", tongs(n))