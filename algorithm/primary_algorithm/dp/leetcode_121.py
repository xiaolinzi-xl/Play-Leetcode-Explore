class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        min_price = prices[0]
        ans = 0
        for i in range(1, n):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] > min_price:
                ans = max(prices[i] - min_price, ans)
        return ans
