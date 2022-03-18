#30. Substring with Concatenation of All Words

from itertools import permutations
def chuyen_danh_sach_thanh_chuoi(ds):
    chuoi_str = ''
    for i in ds:
        chuoi_str += str(i)
    return chuoi_str

s = "barfoothebarfoothefoothethebarfoo"
words = ["bar", "foo", "the","the"]
words_chuoi=[]
ds_index=[]
a=list(permutations(words))
for i in a:
    words_chuoi.append(chuyen_danh_sach_thanh_chuoi(i))
b=len(words_chuoi[0])
z=0
while z <len(s):
    for i1 in words_chuoi:
        if s[z:z+b]==i1:
            ds_index.append(z)
            z+=1
    z+=1
print(ds_index)

