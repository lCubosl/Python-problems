# 739. Daily Temperatures

# brute force
class Solution():
  def dailyTemperatures(self, temperatures):
    answer = []
    l_temperatures = len(temperatures)

    for val in range(l_temperatures):
      count = 1
      next_day = val + 1
      while next_day < l_temperatures:
        if temperatures[next_day] > temperatures[val]:
          break
        next_day += 1
        count +=1
      count = 0 if next_day == l_temperatures else count
      answer.append(count)
      
    return answer
  
# stack
class StackSolution():
  def dailyTemperatures(self, temperatures):  
    answer = [0] * len(temperatures)
    stack = [] 
    for ind, temp in enumerate(temperatures):
      while stack and temp > stack[-1][0]:
        stackTemp, stackInd = stack.pop()
        answer[stackInd] = ind - stackInd
      stack.append((temp, ind))
    
    return answer


solution = StackSolution()
print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))
#print(solution.dailyTemperatures([73,74,75]))