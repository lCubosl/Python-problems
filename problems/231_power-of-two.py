class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        while n % 2 == 0:
            n //= 2
        return n == 1

s = Solution()

print("Input: 1 ->", s.isPowerOfTwo(1))
print("Input: 16 ->", s.isPowerOfTwo(16))
print("Input: 3 ->", s.isPowerOfTwo(3))
print("Input: 0 ->", s.isPowerOfTwo(0))
print("Input: -8 ->", s.isPowerOfTwo(-8))