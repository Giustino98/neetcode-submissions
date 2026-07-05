from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = Counter(nums)
        heap = []

        for elem,freq in freq_dict.items():
            heapq.heappush(heap,(freq,elem))
            if len(heap) > k: heapq.heappop(heap)
        
        return [elem[1] for elem in heap]