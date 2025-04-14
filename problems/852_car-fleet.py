# 853. car fleet
class Solution():
  def carFleet(self, target, position, speed):
    pair = [[p, s] for p, s in zip(position, speed)]
    stack = []

    for p, s in sorted(pair)[::-1]:
      stack.append((target - p) / s)
      if len(stack) >= 2 and stack[-1] <= stack[-2]:
        stack.pop()
    
    return len(stack)

solution = Solution();
print(solution.carFleet(12, [10,8,0,5,3], [2,4,1,1,3])) # 3
print(solution.carFleet(10, [3], [3])) # 1
print(solution.carFleet(100, [0,2,4], [4,2,1])) # 1
print(solution.carFleet(10, [6,8], [3,2])) # 2