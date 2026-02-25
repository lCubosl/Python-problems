# nums = [1,1,2]
# right answer but it's not replacing in place...
nums = [0,0,1,1,1,2,2,3,3,4]
memo = []
k = 0

for num in nums:
  if num not in memo:
    k += 1
    memo.append(num)
  else:
    k += 1
  
# right answer replacing in place

def removeDupe(nums1):
  l = 0
  for r in range(len(nums1)):
    if nums1[r] != nums1[r-1]:
      nums1[l] = nums1[r]
      l += 1
  return l

print(removeDupe(nums))

class Solution(object):
    def removeDupe(self, nums):
        if not nums:
            return 0

        write = 1

        for read in range(1, len(nums)):
            if nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                write += 1

        return write
    
nums = [0,0,1,1,1,2,2,3,3,4]
s = Solution()
k = s.removeDupe(nums)

print("k =", k)
print("modified:", nums[:k])