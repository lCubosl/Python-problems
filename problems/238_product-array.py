# 238. Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all 
# the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# this is O(nxn) or O(n squared) because product is O(n), productExceptSelf is O(n) so O(n) x O(n) = O(n x n)
def product(num):
    result = 1
    for n in num:
        result *= n
    return result

def productExceptSelf(nums):
  result = []

  for n in range(len(nums)):
    temp = nums[:n] + nums[n+1:]
    result.append(product(temp))

  return result

# print(productExceptSelf([1,2,3,4]))
# print(productExceptSelf([-1,1,0,-3,3]))
# print(productExceptSelf([0,0]))

# O(1) solution
def prduct_O1(num):
  n = len(num)
  result = [1] * n

  pre = 1
  for i in range(n):
    result[i] = pre
    pre *= num[i]
    
  suffix = 1
  for i in range(n -1, -1, -1):
     result[i] *= suffix
     suffix *= num[i]
  
  return result

print(prduct_O1([1,2,3,4]))
print(prduct_O1([-1,1,0,-3,3]))
print(prduct_O1([0,0]))