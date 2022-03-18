#Bài 02: cho trước 1 chuỗi ký tự bất kỳ, hãy đếm xem trong chuỗi có bao nhiêu lần xuất hiện chuỗi con là  "abc".
dem_so_lan = 0
a = input('Mời bạn nhập vào một chuỗi: ')
for i in range(0,len(a)):
    if a[i:i+3]=='abc':
        dem_so_lan +=1
print('Vậy số lần abc xuất hiện là: ',dem_so_lan)

