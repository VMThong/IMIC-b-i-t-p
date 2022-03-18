#Bài 03: Cho một dãy các số tự nhiên, tìm và
# in ra 1 giá trị nhỏ nhất của dãy này và chỉ số ứng với giá trị nhỏ nhất này.

dau_vao=[3,7,9,12,11,131,173,191,7,0,1,22,23]

gia_tri_nho_nhat=min(dau_vao)
for i in dau_vao:
    if i==gia_tri_nho_nhat:
        print(' số nhỏ nhất là: ',gia_tri_nho_nhat)
        print('index số: ',dau_vao.index(gia_tri_nho_nhat))
        break
