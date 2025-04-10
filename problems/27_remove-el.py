#27 Remove element
nums = [3,2,2,3]
val = 3
def removeElement(nums, val):
  p1 = 0
  for p2 in range(len(nums)):
    if nums[p2] != val:
      nums[p1] = nums[p2]
      p1 += 1

  return nums, p1


print(removeElement(nums, val))