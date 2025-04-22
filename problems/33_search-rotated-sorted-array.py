# 33. Search in Rotated Sorted Array

# bst(one pass) time: O(log n), space: O(1)
class Solution():
  def search(self, nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
      m = l + ((r - l) // 2)
      if target == nums[m]:
        return m
      
      if nums[l] <= nums[m]:
        if target > nums[m] or target < nums[l]:
          l = m + 1
        else:
          r = m - 1
      else:
        if target < nums[m] or target > target[r]:
          r = m - 1
        else:
          l = m + 1

    return -1

solution = Solution()
print("expected: 4, output:", solution.search(nums = [4,5,6,7,0,1,2], target = 0))
print("expected: -1, output:", solution.search(nums = [4,5,6,7,0,1,2], target = 3))
print("expected: -1, output:", solution.search(nums = [1], target = 0))
print("---------------------------------------")
