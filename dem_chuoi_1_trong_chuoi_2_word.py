#Bài 08: cho 2 chuỗi ký tự s1 và s2, hãy đếm xem số lần chuỗi s1 cuất hiện trong chuỗi s2 là bao nhiêu lần.
chuoi_1 = 'abcd'
chuoi_2 = 'abcdsfdsfabcddasdabcadasabasdaa'
so_lan_lap = 0
for i in range(0, len(chuoi_2)):
    if chuoi_1[0:len(chuoi_1)] == chuoi_2[i:i + len(chuoi_1)]:
        so_lan_lap += 1
print(so_lan_lap)
