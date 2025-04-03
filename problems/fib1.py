# memo stores already existing values so the function doesn't have to be called for every fib(n)
# time complexity O(N)
memo = {}

def fib(n):
  if n in memo:
    return memo[n]
  if n <= 2:
    result = 1
  else:
    result = fib(n - 1) + fib(n - 2)

  memo[n] = result
  return result

print(fib(7))
print(fib(50))

# alternative bottom up aproach
def fib_alt(n):
  memo_alt = {}
  for i in range(1, n + 1):
    if i <= 2:
      result_alt = 1
    else:
      result_alt = memo_alt[i - 1] + memo_alt[i - 2]
    memo_alt[i] = result_alt
  return memo_alt[n]

print(fib_alt(50))