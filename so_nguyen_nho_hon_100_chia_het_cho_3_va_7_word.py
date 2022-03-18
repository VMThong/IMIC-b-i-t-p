# Bài 04: In ra man hinh cac so nguyên nhỏ hơn 100 và chia hết cho 3 và 7
a=[]
for i in range(0,100):
        if i%3==0 and i%7==0:
            a.append(i)
print(a)
