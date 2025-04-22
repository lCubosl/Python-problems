# 271. Encode and Decode Strings
class Solution():
  def encode(self, strs):
    res = ""
    for s in strs:
      res += str(len(s)) + "#" + s
    
    return res
    
  def decode(self, str):
    res, i = [], 0

    while i < len(str):
      j = i
      while str[j] != "#":
        j += 1
      length = int(str[i:j])
      res.append(str[j + 1 : j + 1 + length])
      i = j + 1 + length
    
    return res

solution = Solution()
print(solution.encode(["neet","code","love","you"]))
print(solution.decode("4#neet4#code4#love3#you"))
print(solution.encode(["we","say",":","yes"]))