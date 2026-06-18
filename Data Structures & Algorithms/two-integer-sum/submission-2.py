class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hashmap.keys():
                return [hashmap[difference], i]
            else:
                hashmap[nums[i]] = i
