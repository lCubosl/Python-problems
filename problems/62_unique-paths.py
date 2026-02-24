class Solution(object):
    def uniquePaths(self, m, n):
        from math import comb
        return comb(m + n - 2, m - 1)

s = Solution()

print("Example 1:")
print("Input: m = 3, n = 7")
print("Output:", s.uniquePaths(3, 7))
print()

print("Example 2:")
print("Input: m = 3, n = 2")
print("Output:", s.uniquePaths(3, 2))