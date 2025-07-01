class Solution(object):
  def majorityElement(self, nums):
    freq = {}

    for num in nums:
      if num in freq:
        freq[num] += 1
      else:
        freq[num] = 1

    count = 0
    majority_key = None
    for num in freq:
      if freq[num] > count:
        count = freq[num]
        majority_key = num
    
    return majority_key


solution = Solution()
print(solution.majorityElement(nums = [3,2,3]))
print(solution.majorityElement(nums = [2,2,1,1,1,2,2]))