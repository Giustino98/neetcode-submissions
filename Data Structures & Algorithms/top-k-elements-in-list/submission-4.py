class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = [[] for i in range(len(nums) + 1)]
        freq_map = Counter(nums)
        res = []

        for key, val in freq_map.items():
            freqs[val].append(key)
        
        for bucket in reversed(freqs):
            for elem in bucket:
                res.append(elem)
                if len(res) == k: return res

