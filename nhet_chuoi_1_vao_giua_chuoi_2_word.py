#Bài 13: Cho trước 2 chuỗi ký tự s1 và s2, hãy chen chuỗi s1 vào chính giữa của chuỗi s2 và in ra kết quả.
import math


def tinh_chan_len(input):
    if input % 2 == 0:
        return True
    else:
        return False


s1 = '12345678asds9'
s2 = 'abdcfgdegf'

chieu_dai_s2 = len(s2)
if tinh_chan_len(chieu_dai_s2) == True:
    a1 = s2[0:int((chieu_dai_s2 / 2))] + s1 + s2[(int((chieu_dai_s2 / 2))):chieu_dai_s2]
    print(a1)
else:
    a2 = s2[0:(math.floor(chieu_dai_s2 / 2))] + s1 + s2[((math.floor(chieu_dai_s2 / 2))):chieu_dai_s2]
    print(a2)
