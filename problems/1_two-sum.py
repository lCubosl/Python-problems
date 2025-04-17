# 1. Two sum

class Solution():
  def twoSum(self, nums, target):
    seen = {}

    for i, num in enumerate(nums):
      diff = target - num
      if diff in seen:
        return[seen[diff], i]
      seen[num] = 1
  
solution = Solution()
print(solution.twoSum(nums = [2,7,11,15], target = 9))