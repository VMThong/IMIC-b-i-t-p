#Given a string s, find the length of the longest substring without repeating characters.
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# Example 4:
#
# Input: s = ""
# Output: 0

# Constraints:
#
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

s = "abcabcbb"
a1={''}
a2=''
a3={0}
a1.remove('')
for z in range(0,len(s)):
    for i in range(z,len(s)):
        a1.add(s[i])
        a2 +=s[i]
        if len(a1)==len(a2):
            chieu_dai_max=len(a1)
            a3.add(chieu_dai_max)
        else:
            a1={''}
            a2=''
            a1.remove('')
            break
print(max(a3))
