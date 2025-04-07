# Given an integer array nums and an integer k, return the k most frequent elements. 
# You may return the answer in any order.

# time complex O(n * log k)
import heapq

Input = [1,1,5,1,2,2,3,4,5,6,7,5,4,5,2,2]
k = 2
memo = {}
heap = []

for num in Input:
  if num in memo:
    memo[num] += 1
  else:
    memo[num] = 1

for key, val in memo.items():
  if len(heap) < k:
    heapq.heappush(heap, (val, key))
  else:
    heapq.heappushpop(heap, (val, key))

print([h[1] for  h in heap])

# time complex O(n) down bellow