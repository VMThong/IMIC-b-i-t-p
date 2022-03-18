import re
pt='[0-9]+'#Cộng là phải có ít nhất một chữ số
data = "toan.tran@gmail.com1234567toangmail.com0734343_@gmail.com2345767toan_tran@gmail.com0000toan@gmail"

a = re.split(pt,data)
print(a)
