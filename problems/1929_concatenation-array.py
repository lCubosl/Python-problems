# 1929. Concatenation of Array

nums = [1,3,2,1]
nums2 = []

while len(nums2) < 2 * len(nums):
  for i in range(len(nums)):
    nums2.append(nums[i])

print(nums2)
print(len(nums2))