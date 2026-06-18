class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for idx,elem in enumerate(nums):
            if target - elem in my_dict: return [my_dict[target-elem],idx]
            my_dict[elem] = idx
        
