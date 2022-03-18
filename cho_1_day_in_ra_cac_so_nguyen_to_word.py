#Bài 02: Cho một dãy số tự nhiên, viết chương trình in ra tất cả các số nguyên tố của dãy này.
dau_vao = [3, 7, 9, 12, 11, 131, 173, 191, 7, 0, 1, 22, 23]
du_tru = []
so_lan_chia_duoc = 0

for z in range(0, len(dau_vao)):
    if dau_vao[z] == 0 or dau_vao[z] == 1:
        continue
    for s in range(1, dau_vao[z] + 1):
        if dau_vao[z] % s == 0 and so_lan_chia_duoc < 3:
            so_lan_chia_duoc += 1
    if so_lan_chia_duoc == 2:
        du_tru.append(dau_vao[z])
        so_lan_chia_duoc = 0
    else:
        so_lan_chia_duoc = 0
print(du_tru)
