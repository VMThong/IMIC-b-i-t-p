#Bài 14: cho trước 2 chuỗi ký tự s1 và s2, hãy kiểm tra chuỗi s1 có phải là con của chuỗi s2 hay không
# nếu từ chuỗi s2 chúng ta xóa bỏ vài ký tự thì sẽ thu được chuỗi s1.

s1 = '2345'
s2 = 'fg12ddfgfd3gu7ytu45bnvb'
s = ''
for i in s1:
    for z in s2:
        if i == z:
            s = s + z
            break
        else:
            continue
if s1 == s:
    print('s1 là con của s2')
else:
    print('s1 không phải con của s2')
