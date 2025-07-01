class Solution(object):
  def intToRoman(self, num):
    # roman / integer
    data = { 1:"I", 4:"IV", 5:"V", 9:"IX" , 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M" }
    res = []

    for value in sorted(data.keys(), reverse=True):
      while num >= value:
        res.append(data[value])
        num -= value
    
    return "".join(res)

solution = Solution()
print(solution.intToRoman(num = 3749))
print(solution.intToRoman(num = 58)) 
print(solution.intToRoman(num = 1994))