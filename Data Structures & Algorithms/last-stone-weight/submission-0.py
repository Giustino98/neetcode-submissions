import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]   #per il max heap
        heapq.heapify(stones)

        while len(stones) > 1:
            diff = (heapq.heappop(stones) * -1) - (heapq.heappop(stones)* -1)
            if diff !=0: heapq.heappush(stones,-diff)

        if stones: return -stones[0]
        else: return 0