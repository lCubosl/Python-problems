class Solution(object):
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                pos1 = i + j
                pos2 = i + j + 1

                total = mul + res[pos2]
                res[pos2] = total % 10
                res[pos1] += total // 10

        result = []
        for digit in res:
            if not (len(result) == 0 and digit == 0):
                result.append(str(digit))

        return "".join(result)

s = Solution()

print(s.multiply("2", "3"))
print(s.multiply("123", "456"))
print(s.multiply("0", "999"))
