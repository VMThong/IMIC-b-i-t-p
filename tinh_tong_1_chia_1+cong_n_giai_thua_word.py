# Bài 13: Cho so tu nhien N bat ki, tính tổng và tin ra kết quả
# của S trong đó S= 1 + 1/(1+2!) + 1/(1+2!+3!) +...+ 1/(1+2!+3!+...+N!)

def giai_thua(n):
    if n==1:
        return 1
    else:
        return (n*giai_thua(n-1))

dau_vao=100
mau_so=0
for i in range(1,dau_vao+1):
        c=1
        for z in range(2,i+1):
            c+=giai_thua(z)
        mau_so+=1/c
        c=1
print(mau_so)
