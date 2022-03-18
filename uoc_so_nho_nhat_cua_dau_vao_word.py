#Bài 08: Cho số tự nhiên N bất kỳ (đã gán trước đó), tìm và in ra ước số nguyên nhỏ nhất của N
dau_vao= 321
a=[]
def is_natural_number(n):
    return isinstance(n, int)

if is_natural_number(dau_vao) == True and dau_vao!=0:
    if dau_vao <0:
        dau_vao=dau_vao*-1
        for i in range(2,dau_vao+1):
            if dau_vao%i==0:
                a.append(-i)
    else:
        for i in range(2,dau_vao+1):
            if dau_vao%i==0:
                a.append(i)
    print("Vậy ước số nhỏ nhất của số bạn nhập là: ",min(a))
elif dau_vao == 0 or dau_vao==1:
    print("Không có ước số")

