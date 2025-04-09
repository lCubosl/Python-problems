# You are given an integer array nums and an integer k.

# An integer h is called valid if all values in the array that are strictly greater than h are identical.

# For example, if nums = [10, 8, 10, 8], a valid integer is h = 9 because all nums[i] > 9 are equal to 10,
#  but 5 is not a valid integer.

# You are allowed to perform the following operation on nums:

# 1. Select an integer h that is valid for the current values in nums.
# 2. For each index i where nums[i] > h, set nums[i] to h.

# Return the minimum number of operations required to make every element in nums equal to k. 
# If it is impossible to make all elements equal to k, return -1.

# nums = [5,2,5,4,5]
# k = 2
# unique = set()

# if min(nums) < k:
#   print(-1)

# for n in range(len(nums)):
#   if n > k:
#     unique.add(nums[n])

# print("set lenght: ",len(unique))  

def m_operations(nums, k):
  temp = []
  if min(nums) < k:
    return -1
  
  for n in nums:
    if n > k:
      temp.append(n)
  
  unique = set(temp)
  return len(unique)

print(m_operations([5,2,5,4,5], 2)) # expected output: 2 
print(m_operations([2,1,2], 2)) # expected output: -1
print(m_operations([9,7,5,3], 2)) # expected output: 4