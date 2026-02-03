class Solution(object):
    def countAndSay(self, n):
        s = "1"

        for _ in range(n - 1):
            result = []
            i = 0

            while i < len(s):
                count = 1
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    count += 1
                    i += 1

                result.append(str(count))
                result.append(s[i])
                i += 1

            s = "".join(result)

        return s

s = Solution()

print(s.countAndSay(1))
print(s.countAndSay(2))
print(s.countAndSay(3))
print(s.countAndSay(4))
print(s.countAndSay(5))
