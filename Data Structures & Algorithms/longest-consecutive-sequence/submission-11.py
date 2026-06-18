class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        lengths = []
        for idx, num in enumerate(set_nums):
            curr_length = 1 
            if num - 1 not in set_nums: # verifico se è un potenziale inizio sequenza
               while num + 1 in set_nums:
                    curr_length += 1
                    num += 1
            lengths.append(curr_length)
        
        return max(lengths) if len(lengths) > 0 else 0