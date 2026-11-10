#Bài 1: Viết hàm tìm giá trị lớn nhất trong 3 số
def lonnhat(a,b,c):
    return max(a,b,c)
print(lonnhat(2,4,7))
#cách 2
def max3so(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else :
        return c
print("giá trị lớn nhất:",max3so(2,4,7))
