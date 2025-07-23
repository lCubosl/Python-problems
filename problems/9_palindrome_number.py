class Solution(object):
  def isPalindrome(self, x):
    number_arr = [n for n in str(x)] # O(n)
    reversed_arr = number_arr[::-1]

    if number_arr == reversed_arr:
      return True
    return False
  
  def isPalindrome(self, x):
    number_arr = [n for n in str(x)]
    l, r = 0, len(number_arr) - 1

    while l < r:
      if number_arr[l] != number_arr[r]:
        return False
      l += 1
      r -= 1

    return True

solution = Solution()
print(solution.isPalindrome(x = 121 ))
print(solution.isPalindrome(x = -121 ))
print(solution.isPalindrome(x = 10 ))
print("---------------------------------------")