#Bài 04: Cho trước 1 chuỗi ký tự là họ tên người đầy đủ, hãy tách ra phần họ của người này (họ là từ nằm đầu tiên của chuỗi bao gồm họ và tên)
a = input('Mời bạn nhập vào họ tên đầy đủ: ')
a1=''
for i in range(0,len(a)):
    if a[i]!=" ":
        a1=a1+a[i]
    else:
        break
print('Vậy họ bạn là: ',a1)
