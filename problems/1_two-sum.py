# 1. Two sum

# brute force
class Solution():
  def twoSum1(self, nums, target):
    for i in range(len(nums)):
      for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
          return [i, j]
    
    return []

solution = Solution()
print(solution.twoSum1(nums = [2,7,11,15], target = 9))
print(solution.twoSum1(nums = [3,2,4], target = 6))
print(solution.twoSum1(nums = [3,3], target = 6))
print("---------------------------------------")

# hash map
class Solution():
  def twoSum2(self, nums, target):
    seen = {}

    for i, num in enumerate(nums):
      diff = target - num
      if diff in seen:
        return[seen[diff], i]
      seen[num] = i
  
solution = Solution()
print(solution.twoSum2(nums = [2,7,11,15], target = 9))
print(solution.twoSum2(nums = [3,2,4], target = 6))
print(solution.twoSum2(nums = [3,3], target = 6))
print("---------------------------------------")
