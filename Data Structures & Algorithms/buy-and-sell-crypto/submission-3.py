class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0

        L = 0
        R = 1

        profit = max(prices[R] - prices[L],0)
        while (R < len(prices) - 1):
            if prices[L] > prices[R]:
                L = R
            R += 1
            profit = max(profit,prices[R] - prices[L])
        return profit


