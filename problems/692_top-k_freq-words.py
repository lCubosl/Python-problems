# Given an array of strings words and an integer k, return the k most frequent strings.
# Return the answer sorted by the frequency from highest to lowest. Sort the words with 
# the same frequency by their lexicographical order.

# O(n * log k)
import heapq

# Input = ["the","day","is","sunny","the","the","the","sunny","is","is"]
# Input = ["i","love","leetcode","i","love","coding"]
# Input = ["a","b","c","a","b","c"]
Input = ["aaa","aa","a"]
k = 1
memo = {}
heap = []

for n in enumerate(Input):
  if n in memo:
    memo[n] +=  1
  else:
    memo[n] = 1

print("memo: ",memo)

for key, val in memo.items():
  item = (-val,  key)
  print(item)
  heapq.heappush(heap, item)

result = [heapq.heappop(heap)[1] for _ in range(k)]
print(result)
