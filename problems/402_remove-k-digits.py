# 402. Remove k Digits
class Solution():
  def removeKdigits(self, num, k):
    stack = []

    for val in num:
      while k > 0 and stack and stack[-1] > val:
        k -= 1
        stack.pop()
      stack.append(val)

    stack = stack[:len(stack) - k]
    result = "".join(stack)
    result = result.lstrip("0")

    return result if result else "0"

solution = Solution()
print(solution.removeKdigits(num = "1432219", k = 3)) # 1219
print(solution.removeKdigits(num = "10200", k = 1)) # 200
print(solution.removeKdigits(num = "10", k = 2)) # 0