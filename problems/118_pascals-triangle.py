class Solution(object):
    def generate(self, numRows):
        triangle = []

        for i in range(numRows):
            row = [1] * (i + 1)

            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(row)

        return triangle

s = Solution()
s.generate(5)
print(s.generate(5))