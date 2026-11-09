def mo_phong_may_phat_ve():
  tong_ve = 120
  ve_da_ban = 0
  yeu_cau_chap_nhan = 0

  print("=== MÁY PHÁT HÀNH VÉ ===")
  print(f"Số vé ban đầu: {tong_ve}")

  while True:
    so_luong_mua = int(input("\nNhập số lượng cần mua (Nhập 0 để kết thúc): "))

    if so_luong_mua == 0:
      break

    if so_luong_mua < 0:
      print("Số lượng không hợp lệ! Vui lòng nhập lại.")
      continue

    if tong_ve >= so_luong_mua:
      tong_ve -= so_luong_mua
      ve_da_ban += so_luong_mua
      yeu_cau_chap_nhan += 1
      print(f"-> Giao dịch thành công! Đã cấp {so_luong_mua} vé.")
    else:
      print(f"-> Không đủ vé! Số vé hiện có chỉ còn lại: {tong_ve}")

  print("\n===============================")
  print("KẾT QUẢ CUỐI CÙNG:")
  print(f"- Tổng số vé đã bán: {ve_da_ban}")
  print(f"- Số yêu cầu được chấp nhận: {yeu_cau_chap_nhan}")
  print(f"- Số vé còn lại: {tong_ve}")


if __name__ == "__main__":
  mo_phong_may_phat_ve()