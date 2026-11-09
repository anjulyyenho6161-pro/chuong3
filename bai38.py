#Bài 8: Viết hàm thực hiện phép tính cộng, trừ, nhân, chia hai phân số
#Mỗi phân số được biểu diễn dưới dạng tuple (tử_số, mẫu_số).

import math

def rut_gon_phan_so(ps):
    """Rút gọn phân số"""
    tu, mau = ps
    if mau == 0:
        raise ValueError("Mẫu số không thể bằng 0")
    ucln = math.gcd(tu, mau)
    tu //= ucln
    mau //= ucln
    if mau < 0:  # Đảm bảo mẫu luôn dương
        tu = -tu
        mau = -mau
    return (tu, mau)

def cong_phan_so(ps1, ps2):
    tu = ps1[0] * ps2[1] + ps2[0] * ps1[1]
    mau = ps1[1] * ps2[1]
    return rut_gon_phan_so((tu, mau))

def tru_phan_so(ps1, ps2):
    tu = ps1[0] * ps2[1] - ps2[0] * ps1[1]
    mau = ps1[1] * ps2[1]
    return rut_gon_phan_so((tu, mau))

def nhan_phan_so(ps1, ps2):
    tu = ps1[0] * ps2[0]
    mau = ps1[1] * ps2[1]
    return rut_gon_phan_so((tu, mau))

def chia_phan_so(ps1, ps2):
    tu = ps1[0] * ps2[1]
    mau = ps1[1] * ps2[0]
    return rut_gon_phan_so((tu, mau))

# Ví dụ sử dụng:
ps1 = (1, 2)  # 1/2
ps2 = (1, 3)  # 1/3

print("Cộng 1/2 + 1/3 =", cong_phan_so(ps1, ps2))
print("Trừ 1/2 - 1/3 =", tru_phan_so(ps1, ps2))
print("Nhân 1/2 * 1/3 =", nhan_phan_so(ps1, ps2))
print("Chia 1/2 / 1/3 =", chia_phan_so(ps1, ps2))