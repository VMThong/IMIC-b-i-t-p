# Given a string s, return the longest palindromic substring in s.
#
# Example 1:
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
# Input: s = "cbbd"
# Output: "bb"
# Example 3:
# Input: s = "a"
# Output: "a"
# Example 4:
# Input: s = "ac"
# Output: "a"
#
# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters.

s = "121432432a"
if len(s)<1 or len(s)>1000:
    print('Giá trị nằm ngoài giới hạn')
    exit()

a1=''
a3=['']
for z in range(0,len(s)):
    for i in range(z,len(s)):
        a1+=s[i]
        if len(a1)==1:
            a3.append(a1)
        else:
            chieu_dai_cuoi=len(a1)-1
            if a1[0]==a1[chieu_dai_cuoi]:
                a3.append(a1)
                a1=''
                break
            elif i==len(s)-1 and a1[0]!=a1[chieu_dai_cuoi]:
                a1=''

print(max(a3,key=len))
