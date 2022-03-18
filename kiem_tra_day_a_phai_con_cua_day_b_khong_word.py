#Bài 12: Dãy số a được gọi là dãy con của b nếu từ b xóa đi một vài phần tử sẽ thu được a.
#Cho trước 2 dãy số nguyên a,b. Hãy kiểm tra xem a có là dãy con của b hay không?

day_a = [1, 2, 3, 6, 6]
day_b = [7, 3, 1, 6, 9, 5, 2, 6]
day_a_trong = []
day_b_trong = []
so_lan_giong = 0
if len(day_a) >= len(day_b):
    print('Dãy a không phải là dãy con của b')
    exit()
else:
    for i in day_a:
        for z in day_b:
            if i == z:
                day_a_trong.append(i)
                day_b.remove(z)
                break
if sum(day_a) == sum(day_a_trong):
    print('Dãy a là dãy con của b')
else:
    print('Dãy a không phải là dãy con của b')
