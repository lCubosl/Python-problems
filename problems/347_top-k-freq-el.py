# Given an integer array nums and an integer k, return the k most frequent elements. 
# You may return the answer in any order.

# bucket sort O(n)
class Solution(object):
  def topKFrequent1(self, nums, k):
    seen = {}
    freq = [[] for i in range(len(nums) + 1)]

    for num in nums:
      seen[num] = 1 + seen.get(num, 0)
    for num, cnt in seen.items():
      freq[cnt].append(num)

    res = []
    for i in range(len(freq) - 1, 0, -1):
      for num in freq[i]:
        res.append(num)
        if len(res) == k:
          return res

solution = Solution()
print(solution.topKFrequent1(nums = [1,1,1,2,2,3], k = 2))
print(solution.topKFrequent1(nums = [1], k = 1))
print("---------------------------------------")

# sorting time: O(nlogn)
class Solution(object):
  def topKFrequent2(self, nums, k):
    pass

solution = Solution()
print(solution.topKFrequent2(nums = [1,1,1,2,2,3], k = 2))
print(solution.topKFrequent2(nums = [1], k = 1))
print("---------------------------------------")
