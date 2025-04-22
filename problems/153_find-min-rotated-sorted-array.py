# 153. Find Minimum in Rotated Sorted Array

# brute force time: O(n) space O(1)
class Solution():
  def findMin1(self, nums):
    return min(nums)

solution = Solution()
print("expected: 1, output:", solution.findMin1(nums = [3,4,5,1,2]))
print("expected: 0, output:", solution.findMin1(nums = [4,5,6,7,0,1,2]))
print("expected: 11, output:", solution.findMin1(nums = [11,13,15,17]))
print("---------------------------------------")

# brute force time: O(n) space O(1)
class Solution():
  def findMin2(self, nums):
    result = nums[0]
    l, r = 0, len(nums) - 1

    while l <= r:
      if nums[l] < nums[r]:
        result = min(result, nums[l])
        break

      m = l + ((r - l) // 2)
      result = min(result, nums[m])
      if nums[m] >= nums[l]:
        l = m + 1
      else:
        r = m - 1

    return result

solution = Solution()
print("expected: 1, output:", solution.findMin2(nums = [3,4,5,1,2]))
print("expected: 0, output:", solution.findMin2(nums = [4,5,6,7,0,1,2]))
print("expected: 11, output:", solution.findMin2(nums = [11,13,15,17]))
print("---------------------------------------")
