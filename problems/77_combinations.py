class Solution(object):
    def combine(self, n, k):
        result = []

        def backtrack(start, path):
            if len(path) == k:
                result.append(path[:])
                return

            for num in range(start, n + 1):
                path.append(num)
                backtrack(num + 1, path)
                path.pop()

        backtrack(1, [])
        return result

s = Solution()

print(s.combine(4, 2))
print(s.combine(1, 1))
