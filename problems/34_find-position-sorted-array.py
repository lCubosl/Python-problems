class Solution(object):
    def searchRange(self, nums, target):
        def findLeft():
            left, right = 0, len(nums) - 1
            idx = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
                if nums[mid] == target:
                    idx = mid
            return idx

        def findRight():
            left, right = 0, len(nums) - 1
            idx = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
                if nums[mid] == target:
                    idx = mid
            return idx

        return [findLeft(), findRight()]

s = Solution()

print(s.searchRange([5,7,7,8,8,10], 8))  # [3, 4]
print(s.searchRange([5,7,7,8,8,10], 6))  # [-1, -1]
print(s.searchRange([], 0))              # [-1, -1]
