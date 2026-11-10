dssv=[]

def nhapds():
        for i in range(sosv):
            print(f"Nhập sinh viên thứ {i+1} :")
            masv = input("Nhập mã sinh viên: ")
            ten = input("Nhập tên: ")
            toan = float(input("Nhập điểm toán: "))
            ly = float(input("Nhập điểm lý: "))
            hoa = float(input("Nhập điểm hóa: "))
            diemtb = (toan+ly+hoa) / 3
            if diemtb >= 8:
                hocluc = "Giỏi"
            elif diemtb >= 6.5:
                hocluc = "Khá"
            elif diemtb >= 5:
                hocluc = "Trung bình"
            else:
                hocluc = "Yếu"
            sv = {"Masv": masv, "Tên": ten, "dtoan": toan,
                  "dly": ly, "dhoa": hoa, "dtb": diemtb,
                  "Hl": hocluc}
            dssv.append(sv)
def inds():
        for sv in dssv:
            print(sv["Masv"],"--",
            sv["Tên"],"--",
            sv["dtoan"],"--",sv["dly"],"--",
            sv["dhoa"],"--",sv["dtb"],
            "--",sv["Hl"])
def themsv():
    print("Nhập thông tin sinh viên cần thêm: ")
    masv = input("Nhập mã sinh viên: ")
    ten = input("Nhập tên: ")
    toan = float(input("Nhập điểm toán: "))
    ly = float(input("Nhập điểm lý: "))
    hoa = float(input("Nhập điểm hóa: "))
    diemtb = (toan + ly + hoa) / 3
    if diemtb >= 8:
        hocluc = "Giỏi"
    elif diemtb >= 6.5:
        hocluc = "Khá"
    elif diemtb >= 5:
        hocluc = "Trung bình"
    else:
        hocluc = "Yếu"
    sv = {"Masv": masv, "Tên": ten, "dtoan": toan,
          "dly": ly, "dhoa": hoa, "dtb": diemtb,
          "Hl": hocluc}
    dssv.append(sv)
def capnhat(masv):
    for sv in dssv:
        if sv["Masv"] == masv:
            sv["Tên"] = input("Nhập tên mới: ")
            sv["dtoan"] = float(input("Nhập điểm toán mới: "))
            sv["dly"] = float(input("Nhập điểm lý mới: "))
            sv["dhoa"] = float(input("Nhập điểm hóa mới: "))
            diemtb = (sv["dtoan"] + sv["dly"] + sv["dhoa"]) / 3
            sv["dtb"] = diemtb
            if diemtb >= 8:
                sv["Hl"] = "Giỏi"
            elif diemtb >= 6.5:
                sv["Hl"] = "Khá"
            elif diemtb >= 5:
                sv["Hl"] = "Trung bình"
            else:
                sv["Hl"] = "Yếu"
            return
    print("Không tìm thấy mã sinh viên!")

def xoasv(masvxoa):
    for sv in dssv:
        if sv["Masv"] == masvxoa:
            dssv.remove(sv)
            return
    print("Không tìm thấy mã sinh viên!")
def timkiem(tencantim):
    for sv in dssv:
        if sv["Tên"] == tencantim:
            return "có sinh viên cần tìm "
        return"ko tìm thấy sinh viên"
def demsv(tencantim):
    dem = 0
    for sv in dssv:
        if sv["Tên"]==tencantim:
            dem += 1
    return  dem
def sxdtb():
    return sorted(dssv,key=lambda x:x["dtb"])

def sxten():
    return sorted(key=lambda sv: sv["Tên"])
   
def sxmasv():
    sorted(key=lambda sv: sv["Masv"])
   
sosv = int(input("Nhập số lượng sinh viên: "))
nhapds()
print("Danh sách sinh viên ban đầu:")
inds()

themsv()
print("Danh sách sau khi thêm:")
inds()

masv = input("Nhập mã sinh viên cần cập nhật: ")
capnhat(masv)
print("Danh sách sau khi cập nhật:")
inds()

masvxoa = input("Nhập mã sinh viên cần xóa: ")
xoasv(masv)
print("Danh sách sau khi xóa:")
inds()

tencantim = input("Nhập tên sinh viên cần tìm: ")
timkiem(tencantim)
print("đếm số sinh viên" ,tencantim ,"là",demsv(tencantim))
inds()

print("Sắp xếp theo điểm trung bình:")
dssv=sxdtb()
inds()

print("Sắp xếp theo tên:")
dssv=sxten()
inds()

print("Sắp xếp theo mã sinh viên:")
dssv=sxmasv()
inds()
