class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        dp = [0] * (n + 1)
        dp[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            dp[i] = max(dp[i + 1], dp[i + 2] + nums[i])
        return dp[0]
