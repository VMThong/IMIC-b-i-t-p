"""Câu 1: Cho 1 danh sách các số nguyên, hãy viết hàm cho phép nhận vào danh sách và kiểm tra nếu
danh sách đó có phần tử trùng lặp giá trị thì sẽ trả về True.
(Lưu ý: viết dưới hình thức hàm nhận vào tham số là 1 danh sách, và return về True/False)

Ví dụ 1:
Input: nums = [1,2,3,1]
Output: true

Ví dụ 2:
Input: nums = [1,2,3,4]
Output: false
"""

def kiem_tra_trung(*nums):
    so_lan_trung=0
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                so_lan_trung+=1
    if so_lan_trung>0:
        return True
    else:
        return False
a=kiem_tra_trung(1,1,2,3,5)
print(a)
b=kiem_tra_trung(1,2,3,5,9,7,11)
print(b)
