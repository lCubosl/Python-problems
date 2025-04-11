# 2843. Count Symmetric Integers

low = 1
high = 100
x = 0

for n in range(low, high + 1):
  if len(str(n)) % 2 == 0:
    temp = [int(d) for d in str(n)]
    n1 = temp[:len(temp) // 2]
    n2 = temp[len(temp) // 2:]
    print(sum(n1), sum(n2))

    if sum(n1) == sum(n2):
      x += 1      

print(x)