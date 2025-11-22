class Solution(object):
    # horizontal scanning
    def longestCommonPrefixHorizontal(self,strs):
        if not strs:
            return ""
        
        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        
        return prefix
    
    def longestCommonPrefix(self,strs):
        if not strs:
            return ""
        
        for i in range(len(strs[0])):
            ch = strs[0][i]
            for s in strs[1:]:
                if i == len(s) or s[i] != ch:
                    return strs[0][:i]

            return strs

solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))
print(solution.longestCommonPrefix(["dog","racecar","car"] ))
print("---------------------------------------")