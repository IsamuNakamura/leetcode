#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2 :
            return 0
        sell = prices[0]
        profit = 0
        for price in prices:
            if sell > price:
                sell = price
            else:
                profit = max(profit, price - sell)
        return profit

        # 動的計画法
        # n = len(prices)
        # if n < 2:
        #     return 0

        # dp = [0] * n
        # dp[0] = 0
        # min_price = prices[0]
        # for i in range(1, n):
        #     dp[i] = max(dp[i-1], prices[i] - min_price)
        #     min_price = min(min_price, prices[i])
        # return dp[n-1]


# @lc code=end
