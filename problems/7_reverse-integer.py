class Solution(object):
    def reverse(self, x):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        res = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)

        while x > 0:
            digit = x % 10
            x //= 10

            # Overflow check BEFORE updating res
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > 7):
                return 0

            res = res * 10 + digit

        return sign * res

s = Solution()
print(s.reverse(123))
print(s.reverse(-321))
print(s.reverse(21))
        