class Solution:
    def fib(self, N):
        assert N >= 0, '输入错误'
        if N <= 1:
            return N
        a, b = 0, 1
        for _ in range(2, N + 1):
            c = a + b
            a = b
            b = c
        return b
