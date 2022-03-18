#Bài 07: Cho 1 dãy số tự nhiên, hãy tìm 1 số tự nhiên nhỏ nhất mà không bằng bất cứ số
# nào trong dãy trên.(Tìm số nhỏ nhất và không trùng lặp với phần tử khác trong dãy)

dau_vao=[3,7,9,9,1,0,12,11,3,131,173,191,7,0,1,22,23]
so_khong_trung=[]
so_lan_xuat_hien=0
for i in dau_vao:
    for z in dau_vao:
        if i==z and so_lan_xuat_hien<2:
            so_lan_xuat_hien+=1
    if so_lan_xuat_hien==1:
        so_khong_trung.append(i)
        so_lan_xuat_hien=0
    else:
        so_lan_xuat_hien=0
print(min(so_khong_trung))
