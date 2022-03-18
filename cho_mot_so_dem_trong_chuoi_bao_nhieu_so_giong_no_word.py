# Bài 09: Cho một dãy số nguyên bất kỳ và 1 số cho trước c, hãy đếm có bao nhiêu số trong dãy có giá trị bằng c
dau_vao = [3, 7, 9, 12, 22, 23, 11, 131, 173, 191, 7, 0, 1, 22, 23, 1, 1]
target = 1
so_gia_tri_bang = 0
for i in dau_vao:
    if i == target:
        so_gia_tri_bang += 1
print(so_gia_tri_bang)
