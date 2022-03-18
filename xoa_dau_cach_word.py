#Bài 01:Cho 1 chuỗi ký tự do người dùng nhập vào từ màn hình, trong quá trình nhập,
# người dùng có thể nhập thừa một vài dấu cách,
# hãy xóa những dấu cách thừa và in ra một chuỗi hoàn chỉnh là họ tên của người đó.

dau_vao = 'vo manh thong'
viet_lai = ''
for i in range(0, len(dau_vao)):
    if dau_vao[i] == ' ':
        viet_lai += ''
    else:
        viet_lai += dau_vao[i]
print(viet_lai)
