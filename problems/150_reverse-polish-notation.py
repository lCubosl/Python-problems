# 150. Evaluate Reverse Polish Notation
class Solution:
  def evalRPN(self, tokens):
    numStack = []

    for val in tokens:
      if val not in {"+","-","*","/"}:
        numStack.append(int(val))
      else:
        temp2 = numStack.pop()
        temp1 = numStack.pop()

        if val == "+":
          numStack.append(temp1 + temp2)
          print(temp1, temp2, val)
        elif val == "-":
          numStack.append(temp1 - temp2)
          print(temp1, temp2, val)
        elif val == "*":
          numStack.append(temp1 * temp2)
          print(temp1, temp2, val)
        elif val == "/":
          numStack.append(int(temp1 / float(temp2)))
          print(temp1, temp2, val)

    return numStack[0]

solution = Solution()
# solution.evalRPN(["2","1","+","3","*"])
# print(solution.evalRPN(["2","1","+","3","*"]))
# solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print(solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))