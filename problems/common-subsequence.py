#base case: L(any, 0) = L(0, any) = 0

def longest_common_subsequence(m, n):
  memo = {}

  def lcs(i, j):
    if i == 0 or j == 0:
      return 0
    if (i, j) in memo:
      return memo[(i, j)]
    if m[i-1] == n[j-1]:
      memo[(i, j)] = 1 + lcs(i-1, j-1)
    else:
      memo[(i, j)] = max(lcs(i-1, j), lcs(i, j-1))
    return memo[(i, j)]
  
  return lcs(len(m), len(n))

print(f"Expected output: 4, Output: ", longest_common_subsequence([6,4,5,9,11], [1,15,4,5,6,9,10,11]))
print(f"Expected output: 0, Output: ", longest_common_subsequence([], [1,15,4,5,6,9,10,11]))
print(f"Expected output: 0, Output: ", longest_common_subsequence([], []))
print(f"Expected output: 5, Output: ", longest_common_subsequence([1,2,3,4,5], [1,2,3,4,5]))
