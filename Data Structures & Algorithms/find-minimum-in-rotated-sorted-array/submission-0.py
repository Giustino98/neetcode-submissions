# [1,2,3,4,5,6] -> [5,6,1,2,3,4]
# [1,2,3,4,5,6] -> [6,1,2,3,4,5]
# given m, if previous element is greater I'm done and the minimum is m
# if the previous is smaller, update R with m - 1

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + (r-l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
        return nums[l]
            