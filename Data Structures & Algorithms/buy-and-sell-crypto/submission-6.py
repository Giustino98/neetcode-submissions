class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        best_profit = 0

        for R in range(len(prices)):
            if prices[R] < prices[L]: L = R
            best_profit = max(best_profit,prices[R] - prices[L])
        return best_profit

