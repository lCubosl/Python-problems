# 1922. Count good numbers

class Solution():
  def countGoodNumbers(self, n):
    MOD = 10**9 + 7
    odd = n // 2
    even = (n + 1) // 2
    return pow(5, even, MOD) * pow(4, odd, MOD) % MOD

solution = Solution()
print(solution.countGoodNumbers(2))