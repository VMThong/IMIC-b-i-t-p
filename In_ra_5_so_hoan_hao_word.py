# Bài 06: In ra màn hinh 5 so hoàn hảo đầu tiên  (số hoàn hảo là số có tổng bằng các ước của mình kể cả 1)

#Cách 1: tính chay
# so_lan_chia=0
# a=[]
# for i in range(2,40000000+1):
#     for z in range(1, i + 1):
#         if i % z == 0:
#             so_lan_chia += 1
#             if so_lan_chia>2:
#                 for j in range(1,i):
#                     if i%j==0:
#                         a.append(j)
#                 if sum(a)==i:
#                     print(i)
#                     a=[]
#                     break
#                 else:
#                     so_lan_chia=0
#                     a=[]
#                     break
#     if so_lan_chia==2:
#         so_lan_chia=0
#         a=[]

#Cách 2: sử dụng công thức
a=[]
for p in range(1,20):
    so_tu_cong_thuc=(2**(p-1))*((2**p)-1)
    for i in range(1,so_tu_cong_thuc):
            if so_tu_cong_thuc%i==0:
                a.append(i)
    if sum(a)==so_tu_cong_thuc:
        print(so_tu_cong_thuc)
        a=[]
    else:
        a=[]
