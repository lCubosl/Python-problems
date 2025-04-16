class Solution():
  def isPalindrome(self, s):
    l, r = 0, len(s) -1

    while l < r:
      while l < r and not self.alphaNum(s[l]):
        l += 1
      
      while r > l and not self.alphaNum(s[r]):
        r -= 1
      
      if s[l].lower() != s[r].lower():
        return False
      l, r = l+1, r-1

    return True

  def alphaNum(self, char):
    return (ord("A") <= ord(char) <= ord("Z") or
            ord("a") <= ord(char) <= ord("z") or
            ord("0") <= ord(char) <= ord("9"))

solution = Solution()
print(solution.isPalindrome(s = "A man, a plan, a canal: Panama"))
print(solution.isPalindrome(s = "race a car"))
print(solution.isPalindrome(s = "race e car"))