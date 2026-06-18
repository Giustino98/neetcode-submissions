class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_unique_numbers = set()

        for elem in nums:
            if elem in set_unique_numbers: return True
            set_unique_numbers.add(elem)
        return False