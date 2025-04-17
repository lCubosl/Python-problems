# 11. Container with most water

class Solution():
  def maxArea(self, height):
    l, r = 0, len(height) - 1
    res = 0

    while l < r:
      area = min(height[l], height[r]) * (r-l)
      res = max(res, area)

      if height[l] < height[r]:
        l += 1
      else:
        r -= 1
        
    return res

solution = Solution()
print("expected: 49", solution.maxArea(height = [1,8,6,2,5,4,8,3,7]))
print("expected: 36", solution.maxArea(height = [1,7,2,5,4,7,3,6]))
print("expected: 1", solution.maxArea(height = [1,1]))