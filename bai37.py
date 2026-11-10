#Bài 7: Viết hàm phân tích một số ra các thừa số nguyên tố
def phan_tich(n):
    if n < 2:
        print(f"{n} không phân tích được thành thừa số nguyên tố.")
        return
    i = 2
    ket_qua = []

    while i * i <= n:
        while n % i == 0:
            ket_qua.append(str(i))
            n //= i
        i += 1
    if n > 1:
        ket_qua.append(str(n))
    print(" * ".join(ket_qua))
n = int(input("Nhập vào số cần phân tích: "))
print(f"Các thừa số nguyên tố của {n} là: ", end="")
print(phan_tich(n))
