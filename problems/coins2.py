def sum_m(m, coins):
  memo = {}
  memo[0] = 1
  for i in range(1, m+1):
    memo[i] = 0

    for coin in coins:
      subproblem = i - coin
      if subproblem < 0:
        continue

      memo[i] = memo[i] + memo[subproblem]
  
  return memo[m]

print(sum_m(5, [1, 4, 5]))
print(sum_m(87, [1, 4, 5, 8]))