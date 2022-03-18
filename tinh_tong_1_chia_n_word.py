#Bài 11: Cho số tự nhiên N bất kỳ, tính tổng và tin ra kết quả của S trong đó S= 1+ 1/(1+2)+ 1/(1+2+3) + ... + 1/(1+2+3+...+N)

# Cách 1:
# dau_vao = 10 #lên tới trăm ngàn là không chạy được nữa
# a=[1]
# b=[1]
# for i in range(2,dau_vao+1):
#     for z in range(2,i+1):
#         b.append(z)
#     mau_so=1/sum(b)
#     a.append(mau_so)
#     b=[1]
# print(sum(a))

#Cách 2:
# dau_vao = 10000
# mau_so=1
# for i in range(2,dau_vao+1):
#     c=1
#     for z in range(2,i+1):
#         c+=z
#     mau_so +=1/c
#     c=1
# print(mau_so)

#Cách 3: Dùng đệ quy
def lap_cong(n):
    if n==1:
        return 1
    else:
        return (n+lap_cong(n-1))

dau_vao = 10
cong_don=0
mau_so=0
for i in range(1,dau_vao+1):
    cong_don +=lap_cong(i)
    mau_so +=1/cong_don
    cong_don=0
print(mau_so)
