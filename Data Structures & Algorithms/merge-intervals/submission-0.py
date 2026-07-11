class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals_sorted = sorted(intervals, key = lambda x : x[0])
        res = [intervals_sorted[0]]

        for interval in intervals_sorted[1:]:
            if res[-1][1] >= interval[1]:  #absorbe
                continue
            elif res[-1][1] >= interval[0]:
                res[-1][1] = interval[1]
            else:
                res.append(interval)

        return res

            
