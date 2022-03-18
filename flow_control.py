diem_so = float(input('Vui lòng nhập số: ')) #Cho phép người dùng có thể nhập dữ liệu khi chương trình chạy
if diem_so<0 or diem_so>10:
    print('Điểm số không hợp lệ')
elif diem_so>7.5:
    print('Điểm số là', diem_so)
    print('Điểm số tốt')
elif diem_so<=7.5 and diem_so>=7.0:
    print('Điểm số là', diem_so)
    print('Điểm số khá')
elif diem_so>=5 and diem_so<7.0:
    print('Điểm số là', diem_so)
    print('Điểm số trung bình')
else:
    print('Điểm không số hợp lệ')
