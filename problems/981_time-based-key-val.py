# 981. Time Based Key-Value Store

class Solution():
  def __init__(self):
    self.keyStore = {} # list of [val, time]

  def set(self, key, value, timestamp):
    if key not in self.keyStore:
      self.keyStore[key] = []
    self.keyStore[key].append([value, timestamp])

  def get(self, key, timestamp):
    res = ""
    values = self.keyStore.get(key, [])

    l, r = 0, len(values) - 1

    while l <= r:
      m = l + ((r - l) // 2)
      if values[m][1] <= timestamp:
        res = values[m][0]
        l = m + 1
      else:
        r = m - 1
        
    return res

solution = Solution()
solution.set("alice", "happy", 1)
print(solution.get("alice", 1))
print(solution.get("alice", 2))
solution.set("alice", "sad", 3)
print(solution.get("alice", 3))