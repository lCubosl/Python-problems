# You are given a string s consisting only of the characters 'L' and 'R'.

# A balanced substring is a substring that contains an equal number of 'L' and 'R' characters.

# Return the length of the longest balanced substring in s.
# If there is no balanced substring, return 0.

s = "LRRRLLRLRL"
Output = 6

def longestBalancedSubstring(s: str) -> int:
  prefix_sum = 0
  first_seen = {0: -1}
  max_len = 0

  for i, ch in enumerate(s):
      prefix_sum += 1 if ch == 'R' else -1

      if prefix_sum in first_seen:
          max_len = max(max_len, i - first_seen[prefix_sum])
      else:
          first_seen[prefix_sum] = i

  return max_len


print(longestBalancedSubstring("LRRRLLRLRL"))  # ➜ 6
print(longestBalancedSubstring("LLLRRRLR"))    # ➜ 6
print(longestBalancedSubstring("LLLL"))        # ➜ 0
print(longestBalancedSubstring("LRLRLR"))   