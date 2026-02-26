class Solution(object):
    def removeElement(self, nums, val):
        write = 0
        
        for read in range(len(nums)):
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1
                
        return write
    
nums = [3,2,2,3]
val = 3

s = Solution()
k = s.removeElement(nums, val)

print("k =", k)
print("modified array =", nums[:k])

class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        n = len(nums)
        
        while i < n:
            if nums[i] == val:
                nums.pop(i)
                n -= 1
            else:
                i += 1
                
        return n
    
nums = [0,1,2,2,3,0,4,2]
val = 2

s = Solution()
k = s.removeElement(nums, val)

print("k =", k)
print("modified array =", nums[:k])