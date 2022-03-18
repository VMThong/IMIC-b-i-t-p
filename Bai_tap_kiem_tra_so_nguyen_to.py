a=int(input('Nhập vào một số: '))
so_lan_chia_duoc=0
if a<2:
    print('Đây không phải số nguyên tố')
else:
    for i in range(1,a+1):
        if a%i == 0:
            so_lan_chia_duoc+=1
    if so_lan_chia_duoc == 2:
        print('Đây là nguyên tố')
    else:
        print('Đây không phải số nguyên tố')
