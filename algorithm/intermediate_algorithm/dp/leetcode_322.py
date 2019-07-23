class Solution:
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        dp = [2 << 63] * (amount + 1)
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if i >= coins[j] and dp[i - coins[j]] != 2 << 63:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)

        if dp[amount] != 2 << 63:
            return dp[amount]
        return -1
