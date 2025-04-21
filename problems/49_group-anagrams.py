# 49. Group Anagrams

# hash map
class Solution():
  def groupAnagrams(self, strs):
    result = {}

    for s in strs:
      count = [0] * 26
      for c in s:
        count[ord(c) - ord("a")] += 1
      key = tuple(count)

      if key not in result:
        result[key] = []
      result[key].append(s)
    
    return list(result.values())

solution = Solution()
print(solution.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
print(solution.groupAnagrams(strs = [""]))
print(solution.groupAnagrams(strs = ["a"]))
print("---------------------------------------")