#Bài 07: Trong các số tự nhiên  <=100 hãy đếm xem có bao nhiêu số thõa mãn:
# *- Chia het cho 5
# *- Chia 5 du 1
# *- Chia 5 du 2
# *- Chia 5 du 3

a=[]
for i in range(0,100):
        if i%5==0 or i%5 == 1 or i%5 == 2 or i%5 == 3:
            a.append(i)
print(a)
