# You are given a string s consisting only of the characters 'L' and 'R'.

# A balanced substring is a substring that contains an equal number of 'L' and 'R' characters.

# Return the length of the longest balanced substring in s.
# If there is no balanced substring, return 0.

s = "LRRRLLRLRL"
Output = 6

def longestBalancedSubstring(s: str) -> int:
  pass


print(longestBalancedSubstring("LRRRLLRLRL"))  # ➜ 6
print(longestBalancedSubstring("LLLRRRLR"))    # ➜ 6
print(longestBalancedSubstring("LLLL"))        # ➜ 0
print(longestBalancedSubstring("LRLRLR"))   