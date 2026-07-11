class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals_sorted = sorted(intervals, key = lambda x: x[0])
        res = [intervals_sorted[0]]

        for interval in intervals_sorted[1:]:
            if interval[0] > res[-1][1]:   #disgiunti
                res.append(interval)
            
            else:
                res[-1][1] = max(res[-1][1],interval[1])
        
        return res
            
