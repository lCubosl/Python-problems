# 875. Koko Eating Bananas
import math


class Solution():
  def minEatingSpeed(self, piles, h):
    l, r = 1, max(piles)
    res = r

    while l <= r:
      k = l + ((r - l) // 2)
      hours = 0
      for p in piles:
        hours += math.ceil(float(p) / k)
      if hours <= h:
        res = min(res, k)
        r = k - 1
      else:
        l = k + 1
    
    return res

solution = Solution()
print("expected: 4, output:", solution.minEatingSpeed(piles = [3,6,7,11], h = 8))
print("expected: 30, output:", solution.minEatingSpeed(piles = [30,11,23,4,20], h = 5))
print("expected: 23, output:", solution.minEatingSpeed(piles = [30,11,23,4,20], h = 6))
print("---------------------------------------")
