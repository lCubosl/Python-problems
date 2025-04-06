# contains duplicate
# given an integer array nums, return true if any value appears at least twice in the array
# 2 pointer

def contains_dup_2p(nums):
  nums.sort()
  l, r = 0, 1
  while r < len(nums):
    if nums[l] == nums[r]:
      return True
    l +=1
    r +=1
  return False

print("True: ", contains_dup_2p([1,2,3,1]))
print("False: ", contains_dup_2p([1,2,3]))
print("True: ", contains_dup_2p([1,1,1,3,3,4,3,2,4,2]))

# contains duplicate
# given an integer array nums, return true if any value appears at least twice in the array
# stack

def contains_dup_stack(nums):
  stack = []
  for n in nums:
    if n in stack:
      return True
    stack.append(n)
  return False

print("True: ", contains_dup_stack([1,2,3,1]))
print("False: ", contains_dup_stack([1,2,3]))
print("True: ", contains_dup_stack([1,1,1,3,3,4,3,2,4,2]))

# contains duplicate
# given an integer array nums, return true if any value appears at least twice in the array
# set

def contains_dup_set(nums):
  seen = set()
  for n in nums:
    if n in seen:
      return True
    seen.add(n)
  return False

print("True: ", contains_dup_set([1,2,3,1]))
print("False: ", contains_dup_set([1,2,3]))
print("True: ", contains_dup_set([1,1,1,3,3,4,3,2,4,2]))