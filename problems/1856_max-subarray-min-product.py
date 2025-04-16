# 1856. Maximum Subarray Min-Product

class Solution():
  def maxSumMinProduct(self, nums):
    stack = []
    res = 0
    prefix = [0]

    for n in nums:
      prefix.append(prefix[-1] + n)

    for i, n in enumerate(nums):
      newStart = i
      while stack and stack[-1][1] > n:
        start, val = stack.pop()
        total = prefix[i] - prefix[start]
        res = max(res, val* total)
        newStart = start
      stack.append((newStart, n))

    for start, val in stack:
      total = prefix[len(nums)] - prefix[start]
      res = max(res,  val * total)
    
    return res % (10**9 + 7)

solution = Solution()
print(solution.maxSumMinProduct(nums = [1,2,3,2]))
print(solution.maxSumMinProduct(nums = [2,3,3,1,2]))
print(solution.maxSumMinProduct(nums = [3,1,5,6,4,2]))
print(solution.maxSumMinProduct(nums = [5,10,6,10,4,2,1,4,5,2,4,2,7,5,8,6,3,6,6,4]))