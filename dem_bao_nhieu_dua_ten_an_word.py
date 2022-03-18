#Bài 11: Cho danh sách họ tên đầy đủ học sinh, hãy đếm xem có bao nhiêu bạn tên "An"?
ds_ten = ['Nguyễn An', 'Thái Tài','Thái Bảo An','Võ Minh Thông','Đoàn Quốc Thi','An Bảo']


def ham_dao_nguoc_chuoi(chuoi):
    chuoi_dao = ''
    for i in range(0, len(chuoi)):
        chuoi_dao = chuoi[i] + chuoi_dao
    return chuoi_dao


ds_ten = ['Nguyễn An', 'Thái Tài', 'Thái Bảo An', 'Võ Minh Thông', 'Đoàn Quốc Thi', 'An Bảo', 'An An']

a1 = ''
so_nguoi_ten_an = 0
for i in range(0, len(ds_ten)):
    b = ham_dao_nguoc_chuoi(ds_ten[i])
    for z in range(0, len(b)):
        if b[z] != " ":
            a1 = a1 + b[z]
        else:
            break
    if ham_dao_nguoc_chuoi(a1) == 'An':
        so_nguoi_ten_an += 1
        a1 = ''
    else:
        a1 = ''
print('Vậy số bạn tên An là ', so_nguoi_ten_an, ' bạn')
