class Solution:
    def maxSubArray(self, nums):
        # dp[i] = max(dp[i-1]+nums[i],nums[i])
        n = len(nums)
        dp = nums[:]
        ans = dp[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            ans = max(dp[i], ans)
        return ans
