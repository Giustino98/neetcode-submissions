class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        distinct = set(nums)
        max_seq = 0
        for elem in nums:
            if elem - 1 not in distinct:
                counter = 1
                elem += 1
                while elem in distinct:
                    counter +=1
                    elem += 1
                max_seq = max(counter,max_seq)
        return max_seq
