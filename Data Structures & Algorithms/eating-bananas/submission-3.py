#1,2,3,4
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l<r:
            m = l + (r-l) // 2
            hours = 0
            for pile in piles:
                hours += (pile + m - 1) // m
            
            if hours > h:
                l = m + 1
            else:
                r = m
        
        return r
        
        
