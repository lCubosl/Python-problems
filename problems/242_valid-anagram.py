# 242. Valid Anagram

# sorting
class Solution():
  def isAnagram(self, s, t):
    if len(s) != len(t):
      return False
    return sorted(s) == sorted(t)

solution = Solution()
print(solution.isAnagram("abcabcd", "cba"))
print("Expected: true, Output: ", solution.isAnagram(s = "anagram", t = "nagaram"))
print("Expected: false, Output: ", solution.isAnagram(s = "rat", t = "car"))
print("---------------------------------------")

# hash map - time: O(n + m), space: O(1)
class Solution():
  def isAnagram2(self, s, t):
    if len(s) != len(t):
      return False
    
    mapS, mapT = {}, {}

    for i in range(len(s)):
      mapS[s[i]] = 1 + mapS.get(s[i], 0)
      mapT[t[i]] = 1 + mapT.get(t[i], 0)
    
    print(mapS, mapT)
    return mapS == mapT

solution = Solution()
print("Expected: true, Output: ", solution.isAnagram2(s = "anagram", t = "nagaram"))
print("Expected: false, Output: ", solution.isAnagram2(s = "rat", t = "car"))
print("---------------------------------------")

# hash map (array) - time: O(n + m), space: O(1)
class Solution():
  def isAnagram3(self, s, t):
    if len(s) != len(t):
      return False
    
    count = [0] * 26

    for i in range(len(s)):
      count[ord(s[i]) - ord("a")] += 1
      count[ord(t[i]) - ord("a")] -= 1
    
    for val in count:
      if val != 0:
        return False
    return True

solution = Solution()
print("Expected: true, Output: ", solution.isAnagram3(s = "anagram", t = "nagaram"))
print("Expected: false, Output: ", solution.isAnagram3(s = "rat", t = "car"))
print("---------------------------------------")

# set
class Solution():
  def isAnagram4(self, s, t):
    if len(s) != len(t):
      return False
    
    for i in set(s):
      print(set(s))
      if s.count(i) != t.count(i):
        return False
    return True

solution = Solution()
print("Expected: true, Output: ", solution.isAnagram4(s = "anagram", t = "nagaram"))
print("Expected: false, Output: ", solution.isAnagram4(s = "rat", t = "car"))
print("---------------------------------------")

class Solution():
  def isAnagram4(self, s, t):
    if len(s) != len(t):
      return False

    for i in set(s):
      if s.count(i) != t.count(i):
        return False
    
    return True

solution = Solution()
print("Expected: true, Output: ", solution.isAnagram4(s = "anagram", t = "nagaram"))
print("Expected: false, Output: ", solution.isAnagram4(s = "rat", t = "car"))
print("---------------------------------------")