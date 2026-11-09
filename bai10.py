'''
Bài 10: Viết chương trình quản lý sản phẩm
Mỗi sản phẩm có các thuộc tính: Mã SP, Tên SP, Đơn vị tính, Đơn giá (Dùng từ điển để tạo cấu trúc dữ liệu). Thực hiện các yêu cầu:

a) Nhập vào Danh sách sản phẩm.

b) Hiển thị Danh sách sản phẩm vừa nhập.

c) Tìm xem sản phẩm nào có đơn giá cao nhất.

d) Sắp xếp sản phẩm theo Mã SP.
'''
def nhap_danh_sach_san_pham():
    """a) Nhập vào danh sách sản phẩm"""
    danh_sach = []
    n = int(input("Nhập số lượng sản phẩm: "))
    for i in range(n):
        print(f"\nNhập thông tin sản phẩm thứ {i + 1}:")
        ma_sp = input("Nhập Mã SP: ")
        ten_sp = input("Nhập Tên SP: ")
        don_vi_tinh = input("Nhập Đơn vị tính: ")
        don_gia = float(input("Nhập Đơn giá: "))

        sp = {
            "ma_sp": ma_sp,
            "ten_sp": ten_sp,
            "don_vi_tinh": don_vi_tinh,
            "don_gia": don_gia
        }
        danh_sach.append(sp)
    return danh_sach


def hien_thi_san_pham(danh_sach):
    """b) Hiển thị danh sách sản phẩm vừa nhập"""
    if not danh_sach:
        print("Danh sách sản phẩm trống!")
        return
    print("-" * 65)
    print(f"{'Mã SP':<10} | {'Tên sản phẩm':<20} | {'Đơn vị tính':<15} | {'Đơn giá':<10}")
    print("-" * 65)
    for sp in danh_sach:
        print(f"{sp['ma_sp']:<10} | {sp['ten_sp']:<20} | {sp['don_vi_tinh']:<15} | {sp['don_gia']:<10.2f}")
    print("-" * 65)


def tim_sp_don_gia_cao_nhat(danh_sach):
    """c) Tìm sản phẩm có đơn giá cao nhất"""
    if not danh_sach:
        print("Danh sách trống!")
        return
    max_gia = max(sp["don_gia"] for sp in danh_sach)
    print(f"\nSản phẩm có đơn giá cao nhất ({max_gia}):")
    for sp in danh_sach:
        if sp["don_gia"] == max_gia:
            print(
                f"- Mã SP: {sp['ma_sp']}, Tên SP: {sp['ten_sp']}, Đơn vị: {sp['don_vi_tinh']}, Đơn giá: {sp['don_gia']}")


def sap_xep_theo_ma_sp(danh_sach):
    """d) Sắp xếp sản phẩm theo Mã SP"""
    danh_sach.sort(key=lambda x: x["ma_sp"])
    print("\nĐã sắp xếp danh sách theo Mã SP thành công!")


# --- Chương trình chính cho Bài 10 ---
print("=== CHƯƠNG TRÌNH QUẢN LÝ SẢN PHẨM ===")
ds_sp = nhap_danh_sach_san_pham()

print("\n--- DANH SÁCH SẢN PHẨM VỪA NHẬP ---")
hien_thi_san_pham(ds_sp)

tim_sp_don_gia_cao_nhat(ds_sp)

sap_xep_theo_ma_sp(ds_sp)
print("\n--- DANH SÁCH SAU KHI SẮP XẾP THEO MÃ SP ---")
hien_thi_san_pham(ds_sp)