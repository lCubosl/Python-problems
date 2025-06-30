class Solution(object):
  # O(n^3) approach
  def threeSumClosest(self, nums, target):
    n = len(nums)
    # difference initialized as infinity
    min_diff = float("inf")
    res = 0

    # adds all possible triplets (O(n^3))
    for i in range(n-2):
      for j in range(i+1, n-1):
        for k in range(j+1, n):
          curr_sum = nums[i] + nums[j] + nums[k]
          # difference from target to current sum
          curr_diff = abs(curr_sum - target)
          
          # if difference is smaller than current difference, then new_diff is the the current difference
          # min_difference also needs to be updated
          if curr_diff < min_diff:
            res = curr_sum
            min_diff = curr_diff
          # if there are multiple sums that are closest, take maximum one
          elif curr_diff == min_diff:
            res = max(res, curr_sum)
    
    return res
  
  # sort two pointers O(n)
  def threeSumClosest(self, nums, target):
    n = len(nums)
    nums.sort()
    min_diff = float("inf")
    res = 0

    # initialize l, r pointer (i is position 0, l is position 1, r is position 2)
    for i in range(n-2):
      l, r = i+1, n - 1

      while l < r:
        curr_summ = nums[i] + nums[l] + nums[r]

        # same logic as before
        # if difference is smaller than current difference, then new_diff is the the current difference
        # min_difference also needs to be updated 
        if abs(curr_summ - target) < min_diff:
          min_diff = abs(curr_summ - target)
          res = curr_summ
        # if there are multiple sums that are closest, take maximum one
        elif abs(curr_summ - target) == min_diff:
          res = max(res, curr_summ)
        
        # updates r or l pointer
        if curr_summ > target:
          r -= 1
        else:
          l += 1
    
    return res
    

solution = Solution()
print(solution.threeSumClosest(nums = [-1,2,1,-4], target=1))
print(solution.threeSumClosest(nums = [0,0,0], target=1))