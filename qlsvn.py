import random

# 1. Nhập và kiểm tra điều kiện 0 < n < 10
while True:
    n = int(input("Nhập số lượng phần tử n (0 < n < 10): "))
    if 0 < n < 10:
        break
    else:
        print("⚠️ Điều kiện không hợp lệ! n phải lớn hơn 0 và nhỏ hơn 10. Nhập lại!")

# 2. Tự động sinh ngẫu nhiên n số nguyên trong khoảng từ 1 đến 9 (tuân theo điều kiện 0 < số < 10)
danh_sach_so = []
for i in range(n):
    so_ngau_nhien = random.randint(1, 9)
    danh_sach_so.append(so_ngau_nhien)

# 3. Đếm số chẵn, số lẻ và tính tổng chẵn, tổng lẻ
dem_chan = 0
dem_le = 0
tong_chan = 0
tong_le = 0

for so in danh_sach_so:
    if so % 2 == 0:
        print("số chẵn")
        dem_chan += 1
        tong_chan += so
    else:
        print("số lẻ")
        dem_le += 1
        tong_le += so

# 4. In kết quả ra màn hình
print("\n--- KẾT QUẢ PHÂN TÍCH (RANDOM) ---")
print(f"👉 Danh sách các số ngẫu nhiên: {danh_sach_so}")
print(f"👉 Số lượng số chẵn: {dem_chan} | Tổng chẵn: {tong_chan}")
print(f"👉 Số lượng số lẻ: {dem_le} | Tổng lẻ: {tong_le}")
print(f"👉 Số lớn nhất là: {max(danh_sach_so)}, nằm ở vị trí thứ: {danh_sach_so.index(max(danh_sach_so)) + 1}")
print(f"👉 Số nhỏ nhất là: {min(danh_sach_so)}, nằm ở vị trí thứ: {danh_sach_so.index(min(danh_sach_so)) + 1}")