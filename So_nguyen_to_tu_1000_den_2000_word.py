#Bài 03: In ra man hinh các số nguyên tố từ 1000 đến 2000
so_lan_chia=0
a=[]
for i in range(1000,2000+1):
    for z in range(1, 2000 + 1):
        if i % z == 0:
            so_lan_chia += 1
            if so_lan_chia>2:
                so_lan_chia=0
                break
    if so_lan_chia == 2:
        so_lan_chia=0
        a.append(i)
print(a)

