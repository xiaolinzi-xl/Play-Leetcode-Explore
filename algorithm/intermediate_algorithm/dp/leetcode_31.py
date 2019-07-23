class Solution:
    def uniquePaths(self, m, n):
        dp = [[1] * m for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[n - 1][m - 1]
