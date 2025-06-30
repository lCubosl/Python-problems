class Solution(object):
  # O(n)
  def searchInsert(self, nums, target):
    res = 0
    n = len(nums)

    for num in range(n):
      if target > nums[num]:
        res += 1
      else:
        return res
    
    # all elements are smaller than target
    return res


solution = Solution()
print(solution.searchInsert(nums = [1,3,5,6], target=5))
print(solution.searchInsert(nums = [1,3,5,6], target=2))  
print(solution.searchInsert(nums = [1,3,5,6], target=7))  