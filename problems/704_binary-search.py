# 704. Binary Search

class Solution():
  def search(self, nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
      # m = (l + r) // 2 can lead to overflow (in other languages other than python)
      m = l + ((r - l) // 2)
      if nums[m] > target:
        r = m - 1
      elif nums[m] < target:
        l =  m + 1
      else:
        return m
    
    return -1
      
solution = Solution()
print("expected: 4, output:", solution.search(nums = [-1,0,3,5,9,12], target = 9))
print("expected: -1, output:", solution.search(nums = [-1,0,3,5,9,12], target = 2))
print("expected: -1, output:", solution.search(nums = [-1,0,3,5,9,12], target = -3))
print("expected: 1, output:", solution.search(nums = [-3,0,3,5,9,12], target = 0))
print("---------------------------------------")
