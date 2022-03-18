#Bài 05: In ra màn hình các số nằm giữa 200 va 1000, đồng thời chia hết cho 3,5,7
a=[]
for i in range(200,1000+1):
        if i%105==0:
            a.append(i)
print(a)
