# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# Example 3:
# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000
# Example 4:
# Input: nums1 = [], nums2 = [1]
# Output: 1.00000
# Example 5:
# Input: nums1 = [2], nums2 = []
# Output: 2.00000
#
# Constraints:
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6

nums1 = [5, 2, 1]
m = len(nums1)
nums2 = [3, 3]
n = len(nums2)

if m < 0 or m > 1000:
    print('Giá trị nằm ngoài giới hạn')
    exit()
if m + n < 1 or m + n > 2000:
    print('Giá trị nằm ngoài giới hạn')
    exit()
for i in range(0, len(nums1)):
    if nums1[i] < -10 ** 6 or nums1[i] > 10 ** 6:
        print('Giá trị nằm ngoài giới hạn')
        exit()
for j in range(0, len(nums2)):
    if nums2[j] < -10 ** 6 or nums2[j] > 10 ** 6:
        print('Giá trị nằm ngoài giới hạn')
        exit()


def findMiddle(input_list):
    middle = float(len(input_list)) / 2
    if middle % 2 != 0:
        return input_list[int(middle - .5)]
    else:
        return (input_list[int(middle)], input_list[int(middle - 1)])


def Average(lst):
    return sum(lst) / len(lst)


num_tong = sorted(set(nums1 + nums2))
if len(num_tong) % 2 != 0:
    print(findMiddle(num_tong))
elif len(num_tong) == 2:
    print(Average(num_tong))
else:
    if len(num_tong) % 4 == 0:
        list_1 = findMiddle(num_tong)
        print(Average(list_1))
    else:
        list_1 = (findMiddle(num_tong))
        index_1 = list_1[0]
        index_2 = num_tong.index((index_1)) + 1
        list_1.add(index_2)
        print(Average(list_1))
