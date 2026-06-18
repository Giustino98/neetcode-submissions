from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_freq_dict = defaultdict(int)
        for elem in nums:
            my_freq_dict[elem] += 1
        
        my_keys_list = [x for x in my_freq_dict.keys()]
        my_keys_list.sort(key = lambda key : my_freq_dict[key], reverse = True)
        return my_keys_list[:k]
        
        