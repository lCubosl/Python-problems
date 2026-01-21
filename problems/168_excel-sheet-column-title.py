class Solution(object):
    def convertToTitle(self, columnNumber):
        result = []

        while columnNumber > 0:
            columnNumber -= 1
            result.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26

        return ''.join(reversed(result))


s = Solution()
print(s.convertToTitle(1))    # A
print(s.convertToTitle(28))   # AB
print(s.convertToTitle(701))  # ZY
