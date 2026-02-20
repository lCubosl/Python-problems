class Solution(object):
    def restoreIpAddresses(self, s):
        res = []

        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    res.append(".".join(path))
                return

            for length in range(1, 4):
                if start + length > len(s):
                    break

                segment = s[start:start + length]

                if segment.startswith("0") and len(segment) > 1:
                    continue

                if int(segment) > 255:
                    continue

                backtrack(start + length, path + [segment])

        backtrack(0, [])
        return res

s = Solution()

print("Example 1:")
print("Input: '25525511135'")
print("Output:", s.restoreIpAddresses("25525511135"))
print()

print("Example 2:")
print("Input: '0000'")
print("Output:", s.restoreIpAddresses("0000"))
print()

print("Example 3:")
print("Input: '101023'")
print("Output:", s.restoreIpAddresses("101023"))