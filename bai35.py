#Bài 5: Viết hàm tìm số Fibonacci thứ NTheo định nghĩa trong đề bài:
# $F(0)=0, F(1)=1, F(2)=1, F(3)=2, F(N) = F(N-1) + F(N-2)
def fibonacci(n):
    """Tìm số Fibonacci thứ n"""
    if n < 0:
        return "N phải lớn hơn hoặc bằng 0"
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


# Ví dụ sử dụng:
n = 6
print(f"Số Fibonacci thứ {n} là:", fibonacci(n))