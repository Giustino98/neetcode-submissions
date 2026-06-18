class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for index, elem in enumerate(nums):
            for index1, elem1 in enumerate(nums):
                if elem == elem1 and index != index1:
                    return True
        return False

