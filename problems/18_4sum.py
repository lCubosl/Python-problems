class Solution(object):
  # O(n^4) approach
  def fourSum(self, nums, target):
    res = []

    n = len(nums)
    for i in range(n-3):
      for j in range(i+1, n-2):
        for k in range(j+1, n-1):
          for l in range(k+1, n):
            # count = 0
            if nums[i] + nums[j] + nums[k] + nums[l] == target:
              seen = [nums[i],nums[j],nums[k],nums[l]]
              seen.sort()

              if seen not in res:
                res.append(seen)
              #seen.add([nums[i],nums[j],nums[k],nums[l]])
    
    return res
  
  # 2 pointer O(n^3)
  def fourSum(self, nums, target):
    res = []
    nums.sort()
    
    n = len(nums)
    for i in range(n):
      # skips duplicates for i
      if i>0 and nums[i] == nums[i-1]:
        continue
      
      for j in range(i+1, n):
        # skips duplicates for j
        if j> i+1 and nums[j] == nums[j-1]:
          continue

        # two pointers
        l, r = j+1, n-1
        while l < r:
          total = nums[i] + nums[j] + nums[r] + nums[l]

          if total == target:
            res.append([nums[i], nums[j], nums[r], nums[l]])
            l += 1
            r -= 1

            while l < r and nums[l] == nums[l-1]:
              l += 1
            while l < r and nums[r] == nums[r+1]:
              r -= 1
          elif total < target:
            l += 1
          else:
            r -= 1
      
      return res



solution = Solution()
print(solution.fourSum(nums = [1,0,-1,0,-2,2], target=0))
print(solution.fourSum(nums = [2,2,2,2,2], target=8))
print(solution.fourSum(nums = [10, 2, 3, 4, 5, 7, 8], target=23))