#Bài 12: Cho danh sách họ tên đầy đủ học sinh, hãy đếm xem có bao nhiêu bạn có tên bắt đầu bằng chữ “H”.

def ham_dao_nguoc_chuoi(chuoi):
    chuoi_dao = ''
    for i in range(0, len(chuoi)):
        chuoi_dao = chuoi[i] + chuoi_dao
    return chuoi_dao


ds_ten = ['Nguyễn Hân', 'Nguyễn An', 'Thái Hài', 'Thái Bảo An', 'Võ Minh Thông', 'Đoàn Quốc Hi', 'An Bảo', 'An Hi']

a1 = ''
so_nguoi_ten_H = 0
for i in range(0, len(ds_ten)):
    b = ham_dao_nguoc_chuoi(ds_ten[i])
    for z in range(0, len(b)):
        if b[z] != " ":
            a1 = a1 + b[z]
        else:
            break
    if ham_dao_nguoc_chuoi(a1)[0] == 'H':
        so_nguoi_ten_H += 1
        a1 = ''
    else:
        a1 = ''
print('Vậy số bạn bắt đầu bằng chữ H là ', so_nguoi_ten_H, ' bạn')
