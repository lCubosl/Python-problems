# 217. Contains duplicate

# brute force
class Solution():
  def containsDuplicate2(self, nums):
    for i in range(len(nums)):
      for j in range(i+1, len(nums)):
        if nums[i] == nums[j]:
          return True
    
    return False

solution = Solution()
print("Expected: true, Output: ", solution.containsDuplicate2(nums = [1,2,3,1]))
print("Expected: false, Output: ", solution.containsDuplicate2(nums = [1,2,3,4]))
print("Expected: true, Output: ", solution.containsDuplicate2(nums = [1,1,1,3,3,4,3,2,4,2]))
print("---------------------------------------")

# hashset
class Solution():
  def containsDuplicate3(self, nums):
    seen = set()

    for n in nums:
      if n in seen:
        return True
      seen.add(n)
        
    return False

solution = Solution()
print("Expected: true, Output: ", solution.containsDuplicate3(nums = [1,2,3,1]))
print("Expected: false, Output: ", solution.containsDuplicate3(nums = [1,2,3,4]))
print("Expected: true, Output: ", solution.containsDuplicate3(nums = [1,1,1,3,3,4,3,2,4,2]))
print("---------------------------------------")

# set length
class Solution():
  def containsDuplicate4(self, nums):
    return len(set(nums)) < len(nums)

solution = Solution()
print("Expected: true, Output: ", solution.containsDuplicate4(nums = [1,2,3,1]))
print("Expected: false, Output: ", solution.containsDuplicate4(nums = [1,2,3,4]))
print("Expected: true, Output: ", solution.containsDuplicate4(nums = [1,1,1,3,3,4,3,2,4,2]))
print("---------------------------------------")