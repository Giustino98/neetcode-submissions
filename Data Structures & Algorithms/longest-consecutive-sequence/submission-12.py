class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_seq = 0

        for elem in nums:
            if elem - 1 not in nums_set:
                temp_seq = [elem]
                idx = 1
                while elem + idx in nums_set:
                    temp_seq.append(elem + idx)
                    idx += 1
                if len(temp_seq) > max_seq: max_seq = len(temp_seq)

        return max_seq