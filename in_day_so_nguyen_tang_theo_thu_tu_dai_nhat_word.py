#Bài 11: Cho một dãy số nguyên bất kỳ, hãy tìm 1 dãy
# con liên tục tăng đơn điệu mà là dãy con dài nhất trong dãy số trên.
def chuyen_danh_sach_thanh_chuoi(ds):
    chuoi_str = ''
    for i in ds:
        chuoi_str += str(i)
    return chuoi_str


def chuyen_chuoi_thanh_danh_sach(chuoi):
    danh_sach = []
    for i in range(0, len(chuoi)):
        if chuoi[i] == '-':
            so_am = '-' + chuoi[i + 1]
            danh_sach.append(so_am)
            i += 2
        elif chuoi[i - 1] == '-':
            continue
        else:
            danh_sach.append(chuoi[i])
    return danh_sach


dau_vao = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 3, -9, -8, -7, -6, -5, -4, -3]
a1 = []
a3 = []
a4 = {}

for i in range(0, len(dau_vao)):
    for z in range(i, len(dau_vao)):
        a1.append(dau_vao[z])  # a1 sẽ được cộng dồn liên tục, nếu lấy len nó sẽ ra chiều dài max
        if len(a1) == 1:
            continue
        elif len(a1) != 1:
            if a1[len(a1) - 1] != a1[len(a1) - 2] + 1:
                chieu_dai_max = len(a1) - 1
                a3.append(chieu_dai_max)  # a3 dùng để chứa số lượng phần tử tối đa
                a4[chieu_dai_max] = chuyen_danh_sach_thanh_chuoi(a1)
                a1 = []
                break
            elif a1[len(a1) - 1] == a1[len(a1) - 2] + 1 and i == len(dau_vao) - 1:
                chieu_dai_max = len(a1)
                a3.append(chieu_dai_max)  # a3 dùng để chứa số lượng phần tử tối đa
                a4[chieu_dai_max] = chuyen_danh_sach_thanh_chuoi(a1)
                a1 = []
phan_tu_lon_nhat = max(a3)
print('Số lượng phần tử lớn nhất là: ', phan_tu_lon_nhat)
b = a4.get(phan_tu_lon_nhat)
da_sach_lay_lai = chuyen_chuoi_thanh_danh_sach(b)
c = da_sach_lay_lai[0:len(da_sach_lay_lai) - 1]
print('Danh sách con là: ', chuyen_chuoi_thanh_danh_sach(c))
