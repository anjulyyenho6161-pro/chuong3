# Các hàm chức năng Quản lý Sinh viên
danhsach = []

def tinhdtb_hocluc(toan, ly, hoa):
    """Hàm tính điểm trung bình và xếp loại học lực"""
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

def themsv(danhsach, ma_sv, ten, gioi_tinh, tuoi, toan, ly, hoa):
    """Hàm thêm sẵn dữ liệu mẫu để in kết quả"""
    dtb, hoc_luc = tinhdtb_hocluc(toan, ly, hoa)
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
    danhsach.append(sv)

def xoasv_theoma(danhsach, ma):
    """Xóa sinh viên theo Mã SV"""
    for sv in danhsach:
        if sv["ma_sv"] == ma:
            danhsach.remove(sv)
            print(f"Đã xóa sinh viên có mã: {ma}")
            return
    print("Không tìm thấy sinh viên có mã này.")

def timtheoten(danhsach, tukhoa):
    """Tìm kiếm sinh viên theo từ khóa tên"""
    ketqua = [sv for sv in danhsach if tukhoa.lower() in sv["ten"].lower()]
    if ketqua:
        print(f"\nTìm thấy {len(ketqua)} sinh viên phù hợp:")
        hienthids(ketqua)
    else:
        print("Không tìm thấy sinh viên nào phù hợp.")

def sxdtb(danhsach):
    """Sắp xếp sinh viên theo điểm trung bình (giảm dần)"""
    danhsach.sort(key=lambda x: x["dtb"], reverse=True)
    print("Đã sắp xếp danh sách theo điểm trung bình giảm dần.")

def hienthids(danhsach):
    """Hiển thị danh sách sinh viên"""
    if not danhsach:
        print("Danh sách sinh viên hiện đang trống!")
        return
    print("-" * 105)
    print(f"{'Mã SV':<10} | {'Họ Tên':<20} | {'Giới tính':<10} | {'Tuổi':<5} | {'Toán':<6} | {'Lý':<6} | {'Hóa':<6} | {'ĐTB':<6} | {'Học lực':<10}")
    print("-" * 105)
    for sv in danhsach:
        print(f"{sv['ma_sv']:<10} | {sv['ten']:<20} | {sv['gioi_tinh']:<10} | {sv['tuoi']:<5} | {sv['toan']:<6.1f} | {sv['ly']:<6.1f} | {sv['hoa']:<6.1f} | {sv['dtb']:<6.2f} | {sv['hoc_luc']:<10}")
    print("-" * 105)

ds_sinh_vien = []

# 1. Thêm dữ liệu mẫu
themsv(ds_sinh_vien, "SV001", "Nguyen Van An", "Nam", 20, 8.0, 7.5, 8.5)
themsv(ds_sinh_vien, "SV002", "Tran Thi Binh", "Nu", 19, 6.0, 5.5, 6.5)
themsv(ds_sinh_vien, "SV003", "Le Van Cuong", "Nam", 21, 9.0, 9.5, 9.0)

# 2. In danh sách ban đầu
print("=== DANH SÁCH SINH VIÊN BAN ĐẦU ===")
hienthids(ds_sinh_vien)

# 3. Sắp xếp theo điểm trung bình và in kết quả
print("\n=== SAU KHI SẮP XẾP THEO ĐTB ===")
sxdtb(ds_sinh_vien)
hienthids(ds_sinh_vien)

# 4. Tìm kiếm theo tên
print("\n=== KẾT QUẢ TÌM KIẾM 'An' ===")
timtheoten(ds_sinh_vien, "An")

# 5. Xóa sinh viên và in lại danh sách
print("\n=== SAU KHI XÓA 'SV002' ===")
xoasv_theoma(ds_sinh_vien, "SV002")
hienthids(ds_sinh_vien)