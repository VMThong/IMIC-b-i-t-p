print('Phương trình bậc 2 có dạng a*x^2+b*x+c')
a = float(input('Mời bạn nhập giá trị a: '))
b = float(input('Mời bạn nhập giá trị b: '))
c = float(input('Mời bạn nhập giá trị c: '))
import math

delta =b**2-4*a*c

if delta < 0:
    print('Phương trình vô nghiệm')
elif delta ==0:
    nghiem_kep=-b/(2*a)
    print('Phương trình có nghiệm kép là ',nghiem_kep)
elif delta>0:
    nghiem_1= (-b+math.sqrt(delta))/(2*a)
    nghiem_2= (-b-math.sqrt(delta))/(2*a)
    print('Phương trình có nghiệm 1 là ',nghiem_1)
    print('Phương trình có nghiệm 2 là ',nghiem_2)
