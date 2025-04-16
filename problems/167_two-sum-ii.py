# 167. Two Sum II - Input Array Is Sorted

class Solution():
  def twoSum(self, numbers, target):
    l, r = 0, len(numbers) -1

    while l < r:
      curSum = numbers[l] + numbers[r]
      
      if curSum > target:
        r -= 1
      elif curSum < target:
        l += 1
      else:
        return [l+1, r+1]
    
    return []
        

solution = Solution()
print(solution.twoSum(numbers = [2,7,11,15], target = 9))
print(solution.twoSum(numbers = [2,3,4], target = 6))
print(solution.twoSum(numbers = [-1,0], target = -1))