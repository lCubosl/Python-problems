# brute force
class Solution1(object):
    def climbStairs(self, n):
        if n <= 2:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

class Solution2(object):
    def climbStairs(self, n):
        if n <= 2:
            return n

        one = 2  
        two = 1 

        for _ in range(3, n + 1):
            curr = one + two
            two = one
            one = curr

        return one


s = Solution1()
s.climbStairs(2)
print(s.climbStairs(2))