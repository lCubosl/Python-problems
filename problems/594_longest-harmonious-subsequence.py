class Solution(object):
  def findLHS(self, nums):
    # dictionary
    freq = {}

    # build dictionary with number of occurences for each value
    for num in nums:
      if num in freq:
        freq[num] +=1
      else:
        freq[num] = 1
    print("frequency map:", freq)

    # find longest harmonious subsequence
    res = 0
    for key in freq:
      if key + 1 in freq:
        res = max(res, freq[key] + freq[key+1]) 

    return res

solution = Solution()
print("expected: 5", solution.findLHS(nums = [1,3,2,2,5,2,3,7]))
print("expected: 2", solution.findLHS(nums = [1,2,3,4]))  
print("expected: 2", solution.findLHS(nums = [1,2,3,4,5,6]))  
print("expected: 0", solution.findLHS(nums = [1,1,1,1]))  