# stacks
# given a string s containing just the characters (){}[] determine if the input string is valid
# its valid if and only if
# 1. open brackets must be closed by the same type of brackets
# 2. open brackets must be closed in order
# 3. every close bracket has a corresponding open bracket of the same type

s = "([])[]{}"
p_map = {
  ")":"(",
  "}":"{",
  "]":"["
}
stack = []

def isValid():
  for bracket in s:
    if bracket in p_map:
      if not stack:
        return False
      top = stack.pop()
      if p_map[bracket] != top:
        return False
    else:
      stack.append(bracket)
      print(stack)
  if stack:
    return False
  else:
    return True

  
print(isValid())