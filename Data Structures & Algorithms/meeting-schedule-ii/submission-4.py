"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# 0............................40
#     5............25
#          15..20
#                     30..35

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x : x.start)
        n_rooms = []

        for interval in intervals:
            if n_rooms and interval.start >= n_rooms[0]:
                heapq.heappop(n_rooms)
            heapq.heappush(n_rooms,interval.end)
        
        return len(n_rooms)
            