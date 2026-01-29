class Solution(object):
    def divide(self, dividend, divisor):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Edge case: overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine sign
        negative = (dividend < 0) ^ (divisor < 0)

        # Work with positives
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        # Subtract divisor multiples using bit shifts
        while dividend >= divisor:
            temp = divisor
            multiple = 1

            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            quotient += multiple

        return -quotient if negative else quotient

s = Solution()

print(s.divide(10, 3))    # 3
print(s.divide(7, -3))    # -2
print(s.divide(-2147483648, -1))  # 2147483647
