class Solution:
    def climbStairs(self, n):
        if n <= 3:
            return n
        a, b = 1, 2
        for _ in range(2, n):
            c = a + b
            a = b
            b = c
        return b
