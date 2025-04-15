# 1047. remove all adjacent duplicates in string i

class Solution():
  def removeDuplicates(self, s):
    stack = []

    for c in s:
      if stack and stack[-1] == c:
        stack.pop()
      else:
        stack.append(c)
    
    return "".join(stack)

solution = Solution()
print(solution.removeDuplicates(s = "abcd"))
print(solution.removeDuplicates(s = "deeedbbcccbdaa"))
print(solution.removeDuplicates(s = "pbbcggttciiippooaais"))
