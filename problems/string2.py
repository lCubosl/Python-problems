# valid palindrome 2
# Time complexity: O(n x n)
Input1 = "eceec"

s = Input1
si = s[::-1]

def isPalindrome():
  for n in range(len(si)):
    si_temp = si[:n] + si[n+1:]
    print(si_temp)
    if si_temp == si_temp[::-1]:
      return True
    
  if s == s[::-1]:
    return True
  
  return False
  
print(isPalindrome())

# Time complexity: O(n)
def isPalindrome_alt():
  left, right = 0, len(s) - 1
  while left < right:
    if s[left] != s[right]:
      skipLeft, skipRight = s[left+1:right+1], s[left:right]
      return (skipLeft == skipLeft[::-1] or skipRight == skipRight[::-1])
    left, right = left + 1, right - 1
  return True

print(isPalindrome_alt())
