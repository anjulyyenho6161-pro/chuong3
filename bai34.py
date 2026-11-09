#Bài 4: Viết hàm tính giai thừa của một số tự nhiên
def tinhgiaithua(n):
    """Tính n! (n giai thừa)"""
    if n < 0:
        return "Không tồn tại giai thừa cho số âm"
    gt = 1
    for i in range(1, n + 1):
        gt *= i
    return gt

# Ví dụ sử dụng:
print("5! =", tinhgiaithua(5))