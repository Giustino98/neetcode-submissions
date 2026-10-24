class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = 0

        while l<=r:

            k = l + (r-l) // 2

            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k
            
            if hours > h:
                l = k + 1
            else:
                res = k
                r = k - 1
        
        return res



        
        
