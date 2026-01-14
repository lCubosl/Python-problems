class Solution1(object):
    def lengthOfLastWord(self, s):
        i = len(s) - 1
        length = 0

        while i >= 0 and s[i] == ' ':
            i -= 1
        
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        
        return length
    
class Solution2(object):
    def lengthOfLastWord(self, s):
        words = s.split()
        return len(words[-1])

class Solution3(object):
    def lengthOfLastWord(self, s):
        count = 0
        for ch in reversed(s):
            if ch != ' ':
                count += 1
            elif count > 0:
                break
        return count

s = Solution1()
s.lengthOfLastWord("string word")
print(s.lengthOfLastWord("string word"))