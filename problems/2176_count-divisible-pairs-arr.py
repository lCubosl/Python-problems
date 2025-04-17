# 2176. Cout equal and divisible pairs in an array
class Solution():
  # brute force O(n2)
  def countPairs(self, nums, k):
    N = len(nums)
    res = 0

    for i in range(N):
      for j in range(i+1, N):
        if nums[i] == nums[j] and (i * j) % k == 0:
          res += 1
    
    return res

  # hash map
  def countPairs2(self, nums, k):
    h_map = {}
    res = 0

    for i in range(len(nums)):
      val = nums[i]
      if val in h_map:
        for j in h_map[val]:
          if (i * j) % k == 0:
            res += 1
        h_map[val].append(i)
      else:
        h_map[val] = [i]
      
    print(h_map)
    return res
    

solution = Solution()
print(solution.countPairs2(nums = [3,1,2,2,2,1,3], k = 2))
print(solution.countPairs2(nums = [1,2,3,4], k = 1))

# hash map
