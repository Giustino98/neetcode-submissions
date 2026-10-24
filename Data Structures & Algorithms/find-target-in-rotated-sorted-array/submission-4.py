class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r-l) //2

            if nums[m] == target: return m

            if nums[l] <= nums[m]:
                if target >= nums[l] and target <= nums[m]:
                    r = m
                else: l = m + 1
            elif nums[r] >= nums[m]:
                if target >= nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1     

        return -1
            