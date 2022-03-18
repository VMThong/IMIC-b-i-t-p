# from file_test import Solution
#
# e1=Solution()
# a=e1.isPalindrome(12221)

s='ss'
p='s*'
if s==p:
   print(True)
else:
   i=0
   s1=''
   while i < len(s):
        for j in range(0,len(p)):
            if p[j]=='*':
                p[j]==s[i-1]
                if s[i]==p[j]:
                   s1=s1+p[j]
                   i+=1
                   break
            elif s[i]==p[j]:
                 s1=s1+p[j]
                 i+=1
                 break
            else:
                s[i]!=p[j]
