# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes
# ...contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

l1 = [9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]
a1 = ''
a2 = ''
a3 = ''
for i in range(0, len(l1)):
    a1 = str(l1[i]) + a1
for j in range(0, len(l2)):
    a2 = str(l2[j]) + a2
c = int(a1)
d = int(a2)
b = str(c + d)
for z in range(0, len(b)):
    a3 = b[z] + a3
print(list(a3))
