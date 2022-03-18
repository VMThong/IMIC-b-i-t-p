#11. Container With Most Water
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:
#
# Input: height = [1,1]
# Output: 1
# Example 3:
#
# Input: height = [4,3,2,1,4]
# Output: 16
# Example 4:
#
# Input: height = [1,2,1]
# Output: 2

data = [2, 2, 1]
ds_dien_tich = []
for i in range(0, len(data)):
    for j in range(i + 1, len(data)):
        if data[i] <= data[j]:
            dien_tich = data[i] * j
            ds_dien_tich.append(dien_tich)
        elif data[i] > data[j]:
            dien_tich = data[j] * (j - i)
            ds_dien_tich.append(dien_tich)
print(max(ds_dien_tich))
