class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0

        i = 0

        for i in range(len(prices) - 1):
            profit = max(prices[i + 1:])
            difference = profit - prices[i]

            maxprofit = max(maxprofit, difference)
        return maxprofit

        