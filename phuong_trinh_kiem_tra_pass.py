# #Bài 1: Viết chương trình kiểm tra thông tin password do người dùng nhập vào cần đúng định dạng.
# * ít nhất có 1 ký tự viết hoa
# * ít nhất có 1 chữ số
# * ít nhất có 1 ký tự đặc biệt
# * không được vượt quá 3 ký tự số liên tiếp
# Nếu người dùng nhập không đúng thì bắt buộc người dùng phải nhập lại.
#
# ***gợi ý: các bạn có thể viết nhiều pattern để kiểm tra. nếu chuỗi password do người dùng nhập
# vào đều thỏa mãn những pattern trên thì coi như password được so khớp***


import re

data = 'A4%232'
pt1 = '[A-Z]{1}'  # Kiểm tra chữ hoa
pt2 = '[0-9]{3}'  # Kiểm tra 3 số liên tiếp
pt2_1 = '[0-9]{1}'  # Kiểm tra ít nhất 1 số
pt3 = '[\W]{1}'  # Kiểm tra ký tự đặc biệt

a_viet_hoa = re.findall(pt1, data)
a_3_so_lien_tiep = re.findall(pt2, data)
a_chu_so = re.findall(pt2_1, data)
a_ky_tu_dac_biet = re.findall(pt3, data)
if len(a_viet_hoa) == 0:
    print('Mật khẩu không có ít nhất một chữ in hoa')
if len(a_ky_tu_dac_biet) == 0:
    print('Mật khẩu không có ít nhất một ký tự đặc biệt')
    exit()
if len(a_3_so_lien_tiep) != 0:
    print('Mật có 3 số liên tiếp')
    exit()
elif len(a_chu_so) == 0:
    print('Mật khẩu không có số')
    exit()
print(data)
