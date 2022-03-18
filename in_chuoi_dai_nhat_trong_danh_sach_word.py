#Bài 10: cho 1 danh sách gồm nhiều chuỗi. hãy in ra chuỗi có độ dài dài nhất trong danh sách.
ds_chuoi=['fdsfsdf999999999999999999','234234dsfdf','sdfxzcxzvcxv','4543dsfdsf','fcxvvvvvvvvvvvvvvvvv']
ds_tra={}

for i in ds_chuoi:
    do_dai_chuoi=len(i)
    ds_tra[do_dai_chuoi]=i
print(ds_tra.get(max(ds_tra)))
