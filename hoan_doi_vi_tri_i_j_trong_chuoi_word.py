#Bài 09: cho chuỗi s và 2 vị trí i, j. Hãy hoán đổi giá trị ở 2 vị trí i và j trong chuỗi s, nếu 2 vị trí không tồn
# tại trong chuỗi s, thì không làm gì cả và hiện thông báo cho người dùng.
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


chuoi = 'das232vcmhghg2'
i_index = 3
j_index = 7

if i_index > len(chuoi) - 1 or j_index > len(chuoi) - 1:
    print('Không có vị trí này')
    exit()
elif i_index == j_index:
    print(chuoi)
    exit()
else:
    ds = chuyen_chuoi_thanh_danh_sach(chuoi)
    i_chuoi = ds[i_index]
    j_chuoi = ds[j_index]
    ds[i_index] = j_chuoi
    ds[j_index] = i_chuoi
print(chuyen_danh_sach_thanh_chuoi(ds))
