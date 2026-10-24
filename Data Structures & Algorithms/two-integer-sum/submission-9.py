class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for idx,elem in enumerate(nums):
            diff = target - elem
            if diff in my_dict:
                return [my_dict[diff],idx]
            my_dict[elem] = idx