# 2537. Count the Number of Good Subarrays
# hash map for frequency
# l, r pointer to go through different arrays
# sliding window 
class Solution():
  def countGood(self, nums, k):
    n = len(nums)
    l, r = 0, 0
    good_subarrays = 0
    freq = {}
    e_pairs = 0

    while l < n:
      
      while r < n and e_pairs < k:
        if nums[r] not in freq:
          freq[nums[r]] = 0

        freq[nums[r]] += 1
        if freq[nums[r]] >= 2:
          e_pairs += freq[nums[r]] - 1
        r += 1

      if e_pairs >= k:
        good_subarrays += n - r + 1

      freq[nums[l]] -= 1
      if freq[nums[l]] > 0:
        e_pairs -= freq[nums[l]]
      l += 1
    
    return good_subarrays

solution = Solution()
print(solution.countGood(nums = [1,1,1,1,1], k = 10))
print(solution.countGood(nums = [3,1,4,3,2,2,4], k = 2))
print(solution.countGood(nums = [1,5,2,5,3,2,5,6], k = 2))