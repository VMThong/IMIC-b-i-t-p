#Bài 02: In ra màn hình 15 số nguyên tố đầu tiên bắt đầu từ 1
so_lan_chia=0
so_nguyen_to_thu=0
a=[]
for i in range(2,100):
    for z in range(1,i+1):
        if i%z==0:
            so_lan_chia+=1
    if so_lan_chia==2:
        a.append(i)
        so_lan_chia=0
        so_nguyen_to_thu+=1
        if so_nguyen_to_thu ==15:
            break
    else:
        so_lan_chia=0
print(a)
