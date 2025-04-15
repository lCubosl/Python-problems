# 1209. Remove all adjacent duplicates in string ii

class Solution():
  def removeDuplicates(self, s, k):
    stack = []
    res = ""

    for c in s:
      if stack and stack[-1][0] == c:
        stack[-1][1] += 1
      else:
        stack.append([c, 1])
      if stack[-1][1] == k:
        stack.pop()
      
    for char, count in stack:
      res += (char * count)
      
    return res

solution = Solution()
print(solution.removeDuplicates(s = "abcd", k = 2))
print(solution.removeDuplicates(s = "deeedbbcccbdaa", k = 3))
print(solution.removeDuplicates(s = "pbbcggttciiippooaais", k = 2))