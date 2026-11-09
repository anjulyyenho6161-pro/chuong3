def tong_binh_phuong(n):
  if n <= 0:
    return 0
  if n == 1:
    return 1
  return tong_binh_phuong(n - 1) + n * n


# Chương trình chính
if __name__ == "__main__":
  n = int(input("Nhập số nguyên n: "))
  print(f"S({n}) = {tong_binh_phuong(n)}")