# 735. asteroid collision
class Solution():
  def asteroidCollision(self, asteroids):
    stack = []

    for a in asteroids:
      while stack and a < 0 and stack[-1] > 0:
        diff = a + stack[-1]
        if diff < 0:
          stack.pop()
        elif diff > 0:
          a = 0
        else:
          a = 0
          stack.pop()
      if a:
        stack.append(a)

    return stack

solution = Solution()
print(solution.asteroidCollision(asteroids = [5,10,-5]))
print(solution.asteroidCollision(asteroids = [8,-8]))
print(solution.asteroidCollision(asteroids = [10,2,-5]))