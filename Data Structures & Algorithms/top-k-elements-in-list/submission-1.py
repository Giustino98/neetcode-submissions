from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurence_dict = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        for elem in nums:
            occurence_dict[elem] += 1
        for key,value in occurence_dict.items():
            freq[value].append(key)
        
        res = []
        for elem in freq[::-1]:
            for elem1 in elem:
                res.append(elem1)
                if len(res) == k: return res
        
            

        
        