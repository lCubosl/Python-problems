class Solution(object):
    def jump(self, nums):
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps

s = Solution()

print(s.jump([2,3,1,1,4]))  # 2
print(s.jump([2,3,0,1,4]))  # 2
print(s.jump([1,1,1,1]))    # 3
