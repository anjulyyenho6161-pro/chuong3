# 1. Khai báo một Nút (Node) chứa thông tin thiết bị
class Node:
    def __init__(self, ma_tb, ten_tb, so_luong, don_gia):
        self.ma_tb = ma_tb
        self.ten_tb = ten_tb
        self.so_luong = so_luong
        self.don_gia = don_gia
        self.next = None  # Con trỏ trỏ đến nút tiếp theo


# 2. Khai báo danh sách liên kết đơn
class DanhSachThietBi:
    def __init__(self):
        self.head = None  # Nút đầu danh sách

    # Thêm thiết bị vào cuối danh sách
    def them_cuoi(self, ma_tb, ten_tb, so_luong, don_gia):
        moi = Node(ma_tb, ten_tb, so_luong, don_gia)
        if self.head is None:
            self.head = moi
            return

        # Dùng con trỏ p để chạy từ đầu đến cuối danh sách
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = moi

    # Xuất danh sách
    def xuat(self):
        p = self.head
        print("\n--- DANH SÁCH THIẾT BỊ ---")
        while p is not None:
            print(f"Mã: {p.ma_tb} | Tên: {p.ten_tb} | SL: {p.so_luong} | Giá: {p.don_gia}")
            p = p.next  # Cho con trỏ p trỏ sang nút tiếp theo

    # Tìm thiết bị theo mã
    def tim_kiem(self, ma):
        p = self.head
        while p is not None:
            if p.ma_tb == ma:
                return p
            p = p.next
        return None

    # Tính tổng giá trị (số lượng * đơn giá)
    def tong_gia_tri(self):
        tong = 0
        p = self.head
        while p is not None:
            tong += p.so_luong * p.don_gia
            p = p.next
        return tong

    # Đếm số thiết bị có số lượng bằng X
    def dem_theo_sl(self, x):
        dem = 0
        p = self.head
        while p is not None:
            if p.so_luong == x:
                dem += 1
            p = p.next
        return dem