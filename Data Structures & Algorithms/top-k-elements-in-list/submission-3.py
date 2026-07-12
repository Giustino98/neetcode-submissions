from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        output = []

        freq_dict = Counter(nums)

        for elem, freq in freq_dict.items():
            buckets[freq].append(elem)
        
        for bucket in buckets[::-1]:
            for elem in bucket:
                output.append(elem)
                if len(output) == k: return output