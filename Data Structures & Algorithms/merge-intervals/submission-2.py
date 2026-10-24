#[[1,3],[1,5],[6,7]]

# 1............5
# 1.......3        ------> 1...........5
#.                                          6.....7

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        res = []

        for interval in intervals:
            if not res or interval[0] > res[-1][1]:   # not overlapping interval
                res.append(interval)
            else:
                res[-1][1] = max(interval[1],res[-1][1])
        return res

        
        