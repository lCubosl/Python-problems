class Solution(object):
    def isAdditiveNumber(self, num):
        n = len(num)

        for i in range(1, n):
            for j in range(i + 1, n):

                first = num[:i]
                second = num[i:j]

                if (len(first) > 1 and first[0] == '0'):
                    continue

                if self.isValid(first, second, num[j:]):
                    return True

        return False


    def isValid(self, first, second, remaining):
        while remaining:
            third = str(int(first) + int(second))

            if not remaining.startswith(third):
                return False

            remaining = remaining[len(third):]
            first, second = second, third

        return True
    
num = "112358"
s = Solution()
print(s.isAdditiveNumber(num))