#Bài 05: Cho một dãy số tự nhiên, hãy đếm xem phía bên trên có bao nhiêu số nguyên tố, có bao nhiêu hợp số.

dau_vao=[3,7,9,12,11,131,173,191,7,0,1,22,23]
so_nguyen_to=[]
hop_so=[]
so_lan_chia_duoc=0

for z in range(0, len(dau_vao)):
    if dau_vao[z]==0 or dau_vao[z]==1:
        continue
    for s in range(1,dau_vao[z]+1):
        if dau_vao[z]%s==0 and so_lan_chia_duoc <3:
            so_lan_chia_duoc+=1
    if so_lan_chia_duoc==2:
        so_nguyen_to.append(dau_vao[z])
        so_lan_chia_duoc=0
    else:
        hop_so.append(dau_vao[z])
        so_lan_chia_duoc=0
print('Số lượng số nguyên tố là: '+str(len(so_nguyen_to))+' và số lượng hợp số là: '+str(len(hop_so)))
