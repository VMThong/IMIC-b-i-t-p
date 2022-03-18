#Bài 14: Dãy Fibonaxi 1 2 3 ... F(k)=F(k-1) + F(k-2). Tính số Fibonaxi thứ N

chuoi_thu=38
a=[1,1]
n_chuoi_thu_n=''
if chuoi_thu==1 or chuoi_thu==2:
    print("1")
else:
    for i in range(3,chuoi_thu+1):
        so_thu_tu=i
        gia_tri=sum(a)
        a.append(gia_tri)
        if chuoi_thu>so_thu_tu:
            a.remove(a[0])
    print(gia_tri)



