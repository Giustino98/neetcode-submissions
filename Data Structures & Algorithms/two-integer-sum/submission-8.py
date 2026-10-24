class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx1,elem1 in enumerate(nums):
            diff = target - elem1
            idx2 = idx1 + 1
            while idx2 < len(nums):
                if nums[idx2] == diff: return [idx1,idx2]
                idx2 += 1