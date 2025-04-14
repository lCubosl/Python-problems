# 71. simplify path

class Solution():
  # stack method 1
  # goes through each individual character
  def simplifyPath(self, path):
    stack = []
    val = ""

    for char in path + "/":
      if char == "/":
        if val == "..":
          if stack: 
            stack.pop()
        elif val != "" and val != ".":
          stack.append(val)
        val = ""
      else:
        val += char
    
    return "/" + "/".join(stack)
  
  # stack method 2
  # splits into stack every time there is a /
  def simplifyPath2(self, path):
    stack = []
    path = path.split("/")

    for p in path:
      if p == "" or p == ".":
        continue
      if p == "..":
        if stack:
          stack.pop()
      else:
        stack.append(p)

    return "/" + "/".join(stack)

solution = Solution()
print(solution.simplifyPath2("/home/")) # /home
print(solution.simplifyPath2("/home//foo/")) # /home/foo
print(solution.simplifyPath2("/home/user/Documents/../Pictures")) # /home/user/Pictures
print(solution.simplifyPath2("/.../a/../b/c/../d/./")) # /.../b/d