class Solution(object):
    def getHint(self, secret, guess):
        bulls = 0
        cows = 0
        count = [0] * 10   # digit frequency tracker

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                # if previously seen this digit in guess
                if count[int(s)] < 0:
                    cows += 1
                # if previously seen this digit in secret
                if count[int(g)] > 0:
                    cows += 1

                count[int(s)] += 1
                count[int(g)] -= 1

        return str(bulls) + "A" + str(cows) + "B"
    
secret = "1807"
guess  = "7810"

s = Solution()
print(s.getHint(secret, guess))