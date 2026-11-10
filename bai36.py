#Bài 6: Viết hàm kiểm tra 1 số có phải số hoàn hảo hoặc số chính phương không
import math


def kiem_tra_so(n):
    """Kiểm tra số hoàn hảo và số chính phương"""
    # 1. Kiểm tra số chính phương
    can_bac_hai = int(math.isqrt(n))
    la_chinh_phuong = (can_bac_hai * can_bac_hai == n)

    # 2. Kiểm tra số hoàn hảo (tổng các ước thực sự bằng chính nó)
    tong_uoc = sum(i for i in range(1, n) if n % i == 0) if n > 0 else 0
    la_hoan_hao = (tong_uoc == n and n > 0)

    print(f"Số {n}:")
    print(f"- Có phải số chính phương không? {la_chinh_phuong}")
    print(f"- Có phải số hoàn hảo không? {la_hoan_hao}")


