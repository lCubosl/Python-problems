# memoization to avoid recursion. Time complexity O(M*Coins)
def main_ignore_none(a, b):
  if a is None:
    return b
  if b is None:
    return a
  return  min(a,b)

memo = {}

def min_coins(m, coins):
  if m in memo:
    return memo[m]
  
  if m== 0:
    answer = 0
  else:
    answer = None
    for coin in coins:
      subproblem = m - coin
      if subproblem < 0:
        continue
      answer = main_ignore_none(answer, min_coins(subproblem, coins) + 1)

  memo[m] = answer
  return answer

print(min_coins(13, [1, 4, 5]))
print(min_coins(150, [1, 4, 5]))

# bottom up approach
def min_coins_bu(m, coins):
  memo = {}

  memo[0] = 0
  for i in range(1, m+1):
    for coin in coins:
      subproblem = i - coin
      if subproblem < 0:
        continue
      
      memo[i] = main_ignore_none(memo.get(i), memo.get(subproblem) + 1)
  
  return memo[m]

print(min_coins_bu(150, [1, 4, 5]))