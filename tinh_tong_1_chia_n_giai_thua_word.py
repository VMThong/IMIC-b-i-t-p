#Bài 12: Cho số tự nhiên N bất kỳ, tính tổng và tin ra kết quả của S trong đó S = 1 + 1/2! + 1/3! +...+ 1/N!
def giai_thua(n):
    if n==1:
        return 1
    else:
        return (n*giai_thua(n-1))

dau_vao=3
tong_mau=0
for i in range(1,dau_vao+1):
    tong_mau += 1/giai_thua(i)
print(tong_mau)
