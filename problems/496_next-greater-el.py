# Next Greater Element
class Solution():
  def nextGreaterElement(self, nums1, nums2):
    numsI = {n:i for i, n in enumerate(nums1)}
    res = [-1] * len(nums1)
    stack = []

    for i in range(len(nums2)):
      cur = nums2[i]
      while stack and cur > stack[-1]:
        val = stack.pop()
        idx = numsI[val]
        res[idx] = cur
      if cur in numsI:
        stack.append(cur)
    
    return res

solution = Solution()
print(solution.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))
print(solution.nextGreaterElement(nums1 = [2,4], nums2 = [1,2,3,4]))