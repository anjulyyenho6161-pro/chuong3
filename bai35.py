#Bài 5: Viết hàm tìm số Fibonacci thứ NTheo định nghĩa trong đề bài:
# $F(0)=0, F(1)=1, F(2)=1, F(3)=2, F(N) = F(N-1) + F(N-2)
def tinh_fibonacci(n):
    if n < 0:
        return "Vui lòng nhập số nguyên không âm"
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return b


# Kiểm tra chương trình
n = int(input("Nhập số nguyên n để tìm số Fibonacci thứ n: "))
print(f"Số Fibonacci thứ {n} là: {tinh_fibonacci(n)}")
'''f[0]=0
   f[1]=1
   f[n]=f[n-1]+f[n-2] n>=2
   '''
