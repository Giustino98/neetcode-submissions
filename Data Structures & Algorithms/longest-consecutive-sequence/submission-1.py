class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0: return 0

        nums_set = set(nums)
        seq_init = []
        for num in nums:
            if num - 1 not in nums_set: seq_init.append(num)
        

        sequences = [[seq_init[i]] for i in range(0,len(seq_init))]
        for idx, elem in enumerate(seq_init):
            while(elem + 1 in nums_set):
                sequences[idx].append(elem+1)
                elem = elem + 1
        
        return max(len(x) for x in sequences)
