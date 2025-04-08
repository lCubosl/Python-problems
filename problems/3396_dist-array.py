# 3396. Minimum Number of Operations to Make Elements in Array Distinct
# You are given an integer array nums. You need to ensure that the elements in the array are distinct. 
# To achieve this, you can perform the following operation any number of times:
# Remove 3 elements from the beginning of the array. 
# If the array has fewer than 3 elements, remove all remaining elements.
# Note that an empty array is considered to have distinct elements. Return the minimum number of operations
# needed to make the elements in the array distinct.

Input = [1,2,3,4,2,3,3,5,7,8] # expected: 2
# Input = [4,5,6,4,4] # expected: 2
# Input = [6,7,8,9] # expected: 0

seen = set()
def n_times():
  for i in range(len(Input)-1, -1, -1):
    if Input[i] in seen:
      return (i//3)+1
    else:
      seen.add(Input[i])
  return 0

print(n_times())