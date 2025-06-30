class Solution(object):
  # stack solution
  def isValid(self, s):
    # stack
    stack = []
    # all possible choices dictionary
    p_map = {
        ")":"(",
        "}":"{",
        "]":"[",
    }

    for bracket in s:
      if bracket in p_map:
        # edge case where stack is empty, otherwise index error 
        # ex:"]" the stack stays empty so it needs to return false instantly
        if not stack:
          return False
        
        # value is different from top of the stack returns false 
        if p_map[bracket] != stack.pop():
          return False
      else:
        stack.append(bracket)

    # at the end, if stack is empty, returns True, else returns False    
    if stack:
      return False
    else:
      return True 
    
          


solution = Solution()
print(solution.isValid(s = "()"))
print(solution.isValid(s = "()[]{}"))
print(solution.isValid(s = "(]"))
print(solution.isValid(s = "([])"))