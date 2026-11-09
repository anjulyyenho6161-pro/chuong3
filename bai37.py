#Bài 7: Viết hàm phân tích một số ra các thừa số nguyên tố
def phan_tich_thua_so_nguyen_to(n):
    """Phân tích n thành tích các thừa số nguyên tố"""
    if n < 2:
        return f"{n} không có thừa số nguyên tố lớn hơn 1"

    ket_qua = []
    i = 2
    temp = n
    while i * i <= temp:
        while temp % i == 0:
            ket_qua.append(i)
            temp //= i
        i += 1
    if temp > 1:
        ket_qua.append(temp)

    return ket_qua


# Ví dụ sử dụng:
n = 60
print(f"Thừa số nguyên tố của {n} là:", phan_tich_thua_so_nguyen_to(n))