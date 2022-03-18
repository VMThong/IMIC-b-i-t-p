#Bài 03: Cho trước 1 chuỗi ký tự là họ tên người đầy đủ,
# hãy tách ra phần tên của người này (tên là từ nằm sau cuỗi của chuỗi bao gồm họ và tên)
def ham_dao_nguoc_chuoi(chuoi):
    chuoi_dao = ''
    for i in range(0, len(chuoi)):
        chuoi_dao = chuoi[i] + chuoi_dao
    return chuoi_dao


a = 'Vo Manh Thong'
a1 = ''
b = ham_dao_nguoc_chuoi(a)
for i in range(0, len(b)):
    if b[i] != " ":
        a1 = a1 + b[i]
    else:
        break
print('Vậy họ bạn là: ', ham_dao_nguoc_chuoi(a1))
