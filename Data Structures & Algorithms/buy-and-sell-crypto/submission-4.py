class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0

        L = 0
        R = 1

        profit = max(prices[R] - prices[L],0)
        while R < len(prices):
            if prices[L] < prices[R]:
                profit = max(profit,prices[R] - prices[L])
            else:
                L = R
            R += 1
            
        return profit


