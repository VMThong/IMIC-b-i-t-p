#Bài 08: cho 1 dãy các số nguyên bất kỳ,
# hãy xóa đi trong dãy này các số không phải số nguyên tố và in ra các số còn lại trong dãy.
dau_vao=[3,7,9,12,-1,-3,-5,11,-11,0,-1,1]
du_tru = []
so_lan_chia_duoc=0
def kiem_tra_so_duong(n):
    if n<0:
        return False
    else:
        return True
for z in dau_vao:
    if z==0 or z==1 or z==-1:
        continue
    if kiem_tra_so_duong(z)== True:
        for s in range(1,z+1):
            if z%s==0 and so_lan_chia_duoc <3:
                so_lan_chia_duoc+=1
        if so_lan_chia_duoc==2:
            du_tru.append(z)
            so_lan_chia_duoc=0
        else:
            so_lan_chia_duoc=0
    else:
        z1=z*-1
        for s in range(1,z1+1):
            if z1%s==0 and so_lan_chia_duoc <3:
                so_lan_chia_duoc+=1
        if so_lan_chia_duoc==2:
            du_tru.append(z)
            so_lan_chia_duoc=0
        else:
            so_lan_chia_duoc=0
print(du_tru)
