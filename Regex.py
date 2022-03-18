import re
pt='[a-z0-9][a-z0-9_\.]{1,50}@[a-z0-9_\.]{1,50}\.[a-z]{1,3}'
data = "toan.tran@gmail.com toan.tran123@gmail.com toan@cyber123.com. _@gmail.com 123toan_tran@gmail.com " \
       "1234abc@gmail.com toan@123abc.com toan@cyber123.com.vn toangmail.com toan@.com toan@cybercom"

a = re.findall(pt,data)
print(a)
