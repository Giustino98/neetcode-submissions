class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i, interval in enumerate(intervals):
            # Case 1: Current interval is completely before newInterval
            if newInterval[0] > interval[1]:
                res.append(interval)
            
            # Case 2: newInterval is completely before current interval
            elif newInterval[1] < interval[0]:
                res.append(newInterval)
                # Optimization: since the rest are sorted and disjoint,
                # we append everything left and return immediately
                return res + intervals[i:]
            
            # Case 3: There is an overlap, merge current interval into newInterval
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        
        # If we finish the loop, newInterval belongs at the very end
        res.append(newInterval)
        return res