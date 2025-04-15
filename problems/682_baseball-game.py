# 682. Baseball Game

class Solution():
  def calPoints(self, operations):
    stack = []

    for i in operations:
      if i == "+":
        stack.append(stack[-1] + stack[-2])
      elif i == "D":
        stack.append(2* stack[-1])
      elif i == "C":
        stack.pop()
      else:
        stack.append(int(i))
    
    return sum(stack)

solution = Solution()
print(solution.calPoints(["5","2","C","D","+"]))
print(solution.calPoints(["5","-2","4","C","D","9","+","+"]))
print(solution.calPoints(["1","C"]))