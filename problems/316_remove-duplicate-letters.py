class Solution(object):
    def removeDuplicateLetters(self, s):
        last_index = {c: i for i, c in enumerate(s)}
        stack = []
        seen = set()

        for i, char in enumerate(s):
            if char in seen:
                continue

            while stack and char < stack[-1] and i < last_index[stack[-1]]:
                removed = stack.pop()
                seen.remove(removed)

            stack.append(char)
            seen.add(char)

        return "".join(stack)

s = Solution()
print(s.removeDuplicateLetters("bcabc"))
print(s.removeDuplicateLetters("cbacdcbc"))