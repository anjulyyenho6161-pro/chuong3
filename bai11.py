'''Bài 11: Viết chương trình quản lý sinh viên (Chương 2)
Mỗi sinh viên có các thuộc tính: Mã SV, tên, giới tính, tuổi, điểm toán, điểm lý, điểm hóa, điểm trung bình và học lực.
Trong đó:Điểm trung bình là giá trị trung bình của 3 môn toán, lý, hóa.
Học lực được tính như sau:   Giỏi: nếu điểm trung bình lớn hơn hoặc bằng 8.
Khá: nếu điểm trung bình nhỏ hơn 8 và lớn hơn hoặc bằng 6.5.
Trung Bình: nếu điểm trung bình nhỏ hơn 6.5 và lớn hơn hoặc bằng 5.
 Yếu: nếu điểm trung bình nhỏ hơn 5.
 Thực hiện các yêu cầu:
 a) Nhập vào Danh sách sinh viên.
 b) Hiển thị danh sách sinh viên vừa nhập.
 c) Thêm mới sinh viên.d) Xóa sinh viên bởi Mã SV.
 d) (Tiếp) Tìm kiếm sinh viên theo tên.'''


def tinh_dtb_va_hoc_luc(toan, ly, hoa):
    """Tính điểm trung bình và xếp loại học lực"""
    dtb = (toan + ly + hoa) / 3
    if dtb >= 8.0:
        hoc_luc = "Giỏi"
    elif dtb >= 6.5:
        hoc_luc = "Khá"
    elif dtb >= 5.0:
        hoc_luc = "Trung Bình"
    else:
        hoc_luc = "Yếu"
    return round(dtb, 2), hoc_luc


def nhap_danh_sach_sinh_vien():
    """a) Nhập vào Danh sách sinh viên"""
    danh_sach = []
    n = int(input("Nhập số lượng sinh viên: "))
    for i in range(n):
        print(f"\nNhập thông tin cho sinh viên thứ {i + 1}:")
        ma_sv = input("Nhập Mã SV: ")
        ten = input("Nhập Tên SV: ")
        gioi_tinh = input("Nhập Giới tính: ")
        tuoi = int(input("Nhập Tuổi: "))
        toan = float(input("Nhập điểm Toán: "))
        ly = float(input("Nhập điểm Lý: "))
        hoa = float(input("Nhập điểm Hóa: "))

        dtb, hoc_luc = tinh_dtb_va_hoc_luc(toan, ly, hoa)

        sv = {
            "ma_sv": ma_sv,
            "ten": ten,
            "gioi_tinh": gioi_tinh,
            "tuoi": tuoi,
            "toan": toan,
            "ly": ly,
            "hoa": hoa,
            "dtb": dtb,
            "hoc_luc": hoc_luc
        }
        danh_sach.append(sv)
    return danh_sach


def hien_thi_danh_sach_sv(danh_sach):
    """b) Hiển thị danh sách sinh viên vừa nhập"""
    if not danh_sach:
        print("Danh sách sinh viên trống!")
        return
    print("-" * 105)
    print(
        f"{'Mã SV':<10} | {'Họ Tên':<20} | {'Giới tính':<10} | {'Tuổi':<5} | {'Toán':<6} | {'Lý':<6} | {'Hóa':<6} | {'ĐTB':<6} | {'Học lực':<10}")
    print("-" * 105)
    for sv in danh_sach:
        print(
            f"{sv['ma_sv']:<10} | {sv['ten']:<20} | {sv['gioi_tinh']:<10} | {sv['tuoi']:<5} | {sv['toan']:<6.1f} | {sv['ly']:<6.1f} | {sv['hoa']:<6.1f} | {sv['dtb']:<6.2f} | {sv['hoc_luc']:<10}")
    print("-" * 105)


def them_moi_sinh_vien(danh_sach):
    """c) Thêm mới sinh viên"""
    print("\n--- NHẬP THÔNG TIN SINH VIÊN MỚI ---")
    ma_sv = input("Nhập Mã SV: ")
    ten = input("Nhập Tên SV: ")
    gioi_tinh = input("Nhập Giới tính: ")
    tuoi = int(input("Nhập Tuổi: "))
    toan = float(input("Nhập điểm Toán: "))
    ly = float(input("Nhập điểm Lý: "))
    hoa = float(input("Nhập điểm Hóa: "))

    dtb, hoc_luc = tinh_dtb_va_hoc_luc(toan, ly, hoa)

    sv = {
        "ma_sv": ma_sv,
        "ten": ten,
        "gioi_tinh": gioi_tinh,
        "tuoi": tuoi,
        "toan": toan,
        "ly": ly,
        "hoa": hoa,
        "dtb": dtb,
        "hoc_luc": hoc_luc
    }
    danh_sach.append(sv)
    print("Thêm sinh viên mới thành công!")


def xoa_sinh_vien_theo_ma(danh_sach):
    """d) Xóa sinh viên bởi Mã SV"""
    ma = input("\nNhập Mã SV cần xóa: ")
    for sv in danh_sach:
        if sv["ma_sv"] == ma:
            danh_sach.remove(sv)
            print(f"Đã xóa sinh viên có mã {ma} thành công!")
            return
    print("Không tìm thấy sinh viên có mã này.")


def tim_kiem_sinh_vien_theo_ten(danh_sach):
    """d) Tìm kiếm sinh viên theo tên"""
    tu_khoa = input("\nNhập tên sinh viên cần tìm: ").lower()
    ket_qua = [sv for sv in danh_sach if tu_khoa in sv["ten"].lower()]
    if ket_qua:
        print(f"Tìm thấy {len(ket_qua)} sinh viên phù hợp:")
        hien_thi_danh_sach_sv(ket_qua)
    else:
        print("Không tìm thấy sinh viên nào phù hợp.")


# --- Chương trình chính cho Bài 11 ---
print("\n=== CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN (CHƯƠNG 2) ===")
ds_sv = nhap_danh_sach_sinh_vien()

print("\n--- DANH SÁCH SINH VIÊN BAN ĐẦU ---")
hien_thi_danh_sach_sv(ds_sv)

them_moi_sinh_vien(ds_sv)
print("\n--- DANH SÁCH SAU KHI THÊM MỚI ---")
hien_thi_danh_sach_sv(ds_sv)

tim_kiem_sinh_vien_theo_ten(ds_sv)

xoa_sinh_vien_theo_ma(ds_sv)
print("\n--- DANH SÁCH SAU KHI XÓA ---")
hien_thi_danh_sach_sv(ds_sv)