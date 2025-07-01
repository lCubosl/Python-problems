class Solution(object):
  def romanToInt(self, s):
    data = {
      "I": 1,
      "V": 5,
      "X": 10,
      "L": 50,
      "C": 100,
      "D": 500,
      "M": 1000
    }

    # list of roman numbers converted to integers
    characters = []
    for symbol in s:
      characters.append(data[symbol])
    
    # if the romans are in order, return instantly result
    if characters == sorted(characters, reverse=True):
      return sum(characters)
    
    # if the romans are not in order, go through the list in reverse order and subtract the out of order ones
    count = 0
    for num in range(len(characters[::-1]) - 1):
      if characters[num] < characters[num  + 1]:
        count += characters[num]
      
    #print("count",count)
    return sum(characters) - 2*(count)

  # refactor code
  def romanToInt(self, s):
    # dictionary of roman : integers
    data = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }

    res = 0
    remaining = 0

    # reverse the roman number and go through array
    for char in reversed(s):
      value = data[char]
      if value < remaining:
        res -= value
      else:
        res += value
        remaining = value
    
    return res



solution = Solution()
print(solution.romanToInt(s = "III"))
print(solution.romanToInt(s = "LVIII")) 
print(solution.romanToInt(s = "MCMXCIV"))