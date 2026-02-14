class Solution1(object):
    def subsets(self, nums):
        res = []

        def backtrack(start, path):
            res.append(path[:])

            for i in range(start, len(nums)):
                backtrack(i + 1, path + [nums[i]])

        backtrack(0, [])
        return res

class Solution2(object):
    def subsets(self, nums):
        res = [[]]

        for num in nums:
            res += [curr + [num] for curr in res]

        return res

s = Solution1()
print(s.subsets([1,2,3]))
