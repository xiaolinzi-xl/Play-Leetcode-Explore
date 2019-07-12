class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        if n == 0:
            return 1
        if n == 1:
            return x
        if n & 1:
            return x * self.myPow(x, n - 1)
        else:
            tmp = self.myPow(x, n // 2)
            return tmp ** 2
