class Solution(object):
    def hammingWeight(self, n):
        count = 0
        while n:
            n &= n - 1   # removes the lowest set bit
            count += 1
        return count

s = Solution()
print(s.hammingWeight(11))
print(s.hammingWeight(128))
print(s.hammingWeight(2147483645))