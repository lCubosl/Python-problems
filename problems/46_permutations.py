class Solution(object):
    def permute(self, nums):
        res = []
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                backtrack(path + [nums[i]])
                used[i] = False

        backtrack([])
        return res

class Solution1(object):
    def permute(self, nums):
        res = []

        def backtrack(start):
            if start == len(nums):
                res.append(nums[:])
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return res


nums = [1,2,3]
print(Solution().permute(nums))
