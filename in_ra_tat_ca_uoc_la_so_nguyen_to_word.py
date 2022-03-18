#Bài 10: Cho số tự nhiên N bất kỳ (đã gán trước đó), In ra màn hình tất cả các ước(là số nguyên tố) của N

dau_vao= 0
a=[]
a_nguyen_to=[]
so_lan_chia=0
def is_natural_number(n):
    return isinstance(n, int)

if dau_vao == 0 or dau_vao == 1:
    print("Không có ước số")
    exit()
if is_natural_number(dau_vao) == True and dau_vao!=0:
    if dau_vao <0:
        dau_vao=dau_vao*-1
        for i in range(2,dau_vao+1):
            if dau_vao%i==0:
                a.append(-i)
    else:
        for i in range(2,dau_vao+1):
            if dau_vao%i==0:
                a.append(i)

for l in a:
    for z in range(1,l+1):
        if l%z==0 and so_lan_chia<3:
            so_lan_chia+=1
    if so_lan_chia==2:
        a_nguyen_to.append(l)
        so_lan_chia=0
    else:
        so_lan_chia=0
print("Vậy ước số mà là các số nguyên tố= ",a_nguyen_to)


