#Bài 07: Cho trước chuỗi ký tự s bất kỳ, hãy thay thế các ký tự trong chuỗi s là chữ số thành ký tự $, và in ra chuỗi s mới.
dem_so_lan = 0
a = input('Mời bạn nhập vào một chuỗi: ')
a1=''
for i in range(0,len(a)):
    if a[i].isdigit() == True:
        a1=a1+'$'
    else:
        a1=a1+a[i]
print(a1)
