class Solution(object):
    def myAtoi(self, s):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        i = 0
        n = len(s)

        while i < n and s[i] == ' ':
            i += 1

        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        num = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')

            if num > INT_MAX // 10 or (num == INT_MAX // 10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN

            num = num * 10 + digit
            i += 1

        return sign * num

s = Solution()
print(s.myAtoi("42"))
print(s.myAtoi("-42"))
print(s.myAtoi(" -042"))
print(s.myAtoi("1337c0d3"))