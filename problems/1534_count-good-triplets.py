# 1534. Count Good Triplets# 
# brute force approach. Haven't learned sliding windows yet :C

class Solution():
  def countGoodTriplets(self, arr, a, b, c):
    l_arr = len(arr)
    count = 0
    for i in range(l_arr):
      for j in range(i+1, l_arr):
        for k in range(j+1, l_arr):
          if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
            count += 1
    
    return count


solution = Solution()
print(solution.countGoodTriplets([3,0,1,1,9,7], 7, 2, 3)) #4
print(solution.countGoodTriplets([1,1,2,2,3], 0, 0, 1)) #0