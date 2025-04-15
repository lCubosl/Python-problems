# 456. 132 pattern
class Solution():
  def find132pattern(self, nums):
    stack = []
    curMin = nums[0]

    for n in nums[1:]:
      while stack and n >= stack[-1][0]:
        stack.pop()
      if stack and n > stack[-1][1]:
        return True
      stack.append([n,curMin])
      curMin = min(curMin, n)

    return False

solution = Solution()
print(solution.find132pattern([1,2,3,4])) # false
print(solution.find132pattern([3,1,4,2])) # true
print(solution.find132pattern([3,1,4,2])) # true
print(solution.find132pattern([-1,3,2,0])) # true