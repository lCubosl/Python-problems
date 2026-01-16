class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        
        n,m = len(haystack), len(needle)

        for i in range(n-m+1):
            if haystack[i:i+m] == needle:
                return i
        
        return -1

class Solution1(object):
    def strStr(self, haystack, needle):
        if needle == "":
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            j = 0
            while j < len(needle) and haystack[i + j] == needle[j]:
                j += 1
            if j == len(needle):
                return i

        return -1

s = Solution()
s.strStr("sadbutsad", "sad")        
print(s.strStr("sadbutsad", "sad"))