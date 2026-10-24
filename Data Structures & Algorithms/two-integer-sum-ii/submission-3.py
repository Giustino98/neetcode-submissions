class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums_map = {}

        for idx,elem in enumerate(numbers):
            diff = target - elem
            if diff in nums_map: return [nums_map[diff] + 1 , idx + 1]
            nums_map[elem] = idx
    