#Bài 10: Cho 1 dãy số nguyên tố bất kỳ, hãy tìm ra 1 dãy số liền nhau dài nhất bao gồm các số bằng nhau.
# Hãy in ra số lượng phần tử của dãy này và chỉ số index đầu tiên của dãy con này trong dãy lớn.

dau_vao = [1, 0, 1, 0, 0, 9, 9, 9, 9, 9, 9, 0, 0, 0, 3, 3]
a1 = []
a3 = []
a4 = {}

for i in range(0, len(dau_vao)):
    for z in range(i, len(dau_vao)):
        a1.append(dau_vao[z])  # a1 sẽ được cộng dồn liên tục, nếu lấy len nó sẽ ra chiều dài max
        if len(set(a1)) > 1:
            chieu_dai_max = len(a1) - 1
            a3.append(chieu_dai_max)  # a3 dùng để chứa số lượng phần tử tối đa
            a4[chieu_dai_max] = 'Số của phần tử là: ' + str(dau_vao[i]) + ',index thứ ' + str(
                i)  # #a4 dùng chưa dữ liệu dạng dict để lấy được value (số) qua key (max)
            a1 = []
            a2 = []
            break
        elif len(set(a1)) == 1:
            if len(dau_vao) - 1 != z:
                continue
            else:
                chieu_dai_max = len(a1)
                a3.append(chieu_dai_max)
                a4[chieu_dai_max] = 'Số của phần tử là: ' + str(dau_vao[i]) + 'index thứ ' + str(i)
                a1 = []
                a2 = []
phan_tu_lon_nhat = max(a3)
print('Số lượng phần tử lớn nhất là: ', phan_tu_lon_nhat)
b = a4.get(phan_tu_lon_nhat)
print(b)
