class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx1, num1 in enumerate(nums):
            for idx2, num2 in enumerate(nums[idx1 + 1:]):
                if num1 + num2 == target:
                    return [idx1, idx2 + idx1 + 1]
        print("Indexes not found")