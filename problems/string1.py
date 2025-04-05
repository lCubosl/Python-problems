# palindrome checker
import re

Input = "A man, a plan, a canal: Panama"

s = Input.lower()
s = re.sub(r"[^A-Za-z0-9]", "", s)

def isPalindrome():
  return s == s[::-1]


print(isPalindrome())