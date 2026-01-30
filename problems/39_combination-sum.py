class Solution(object):
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, path, remaining):
            if remaining == 0:
                result.append(list(path))
                return

            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, remaining - candidates[i])
                path.pop()

        backtrack(0, [], target)
        return result

s = Solution()

print(s.combinationSum([2,3,6,7], 7))
print(s.combinationSum([2,3,5], 8))
print(s.combinationSum([2], 1))
