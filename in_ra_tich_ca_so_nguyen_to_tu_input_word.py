# Bài 09: Cho số tự nhiên N lớn hơn 1 bất kỳ (đã gán trước đó) , In ra khai triển thành tích các số nguyên tố tính từ nhỏ đến lớn
# *Vd:
# 9--> 3.3
# 12--> 2.2.3
index = []
input1 = 999
tich_so = ''
if input1 == 0:
    print('0')
    exit()
elif input1 == 1:
    print('1')
    exit()
for z in range(2, input1 + 1):
    while input1 % z == 0 and input1 >= z:
            input1 /= z
            index.append(str(z))
sap_lai_list = (sorted(index))
for i in range(0, len(sap_lai_list)):
    tich_so += sap_lai_list[i]
    tich_so +='.'
print(tich_so[0:len(tich_so) - 1])
