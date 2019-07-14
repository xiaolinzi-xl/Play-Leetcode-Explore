class Solution:
    def maxProfit(self, prices):
        index = 0
        flag = False
        ans = 0
        i = 1
        n = len(prices)
        while i < n:
            if prices[i] > prices[i - 1]:
                flag = True
            else:
                if flag:
                    ans += prices[i - 1] - prices[index]
                    flag = False
                index = i
            i += 1
        if flag:
            ans += prices[n - 1] - prices[index]
        return ans


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices))
