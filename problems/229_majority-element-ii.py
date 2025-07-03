class Solution(object):
  def majorityElement(self, nums):
    freq = {}

    for num in nums:
      if num in freq:
        freq[num] += 1
      else:
        freq[num] = 1

    sort_by_key = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))     

    res = []
    # majority element that is appended to the list must be greater than n//3

    for key, val in sort_by_key.items():
      if val > len(nums)//3:
        res.append(key)
      
    return res


solution = Solution()
print("[3]", solution.majorityElement(nums = [3,2,3]))
print("[1]", solution.majorityElement(nums = [1]))
print("[1,2]", solution.majorityElement(nums = [1,2]))