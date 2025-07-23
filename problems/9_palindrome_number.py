class Solution(object):
  def isPalindrome(self, x):
    number_arr = [n for n in str(x)] # O(n)
    reversed_arr = number_arr[::-1]

    if number_arr == reversed_arr:
      return True
    return False

solution = Solution()
print(solution.isPalindrome(x = 121 ))
print(solution.isPalindrome(x = -121 ))
print(solution.isPalindrome(x = 10 ))
print("---------------------------------------")