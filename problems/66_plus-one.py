class Solution(object):
    def plusOne(self, digits):
        n = len(digits)

        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        # If we exit loop, all digits were 9
        return [1] + digits

s = Solution()

print("Example 1:")
print("Input: [1,2,3]")
print("Output:", s.plusOne([1,2,3]))
print()

print("Example 2:")
print("Input: [4,3,2,1]")
print("Output:", s.plusOne([4,3,2,1]))
print()

print("Example 3:")
print("Input: [9]")
print("Output:", s.plusOne([9]))
print()

print("Extra Test:")
print("Input: [9,9,9]")
print("Output:", s.plusOne([9,9,9]))
