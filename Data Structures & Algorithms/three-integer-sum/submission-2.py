"""
a + b + c = 0 -> fixed a -> b + c = -a 
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for idx in range(len(nums) - 2):
            if idx > 0 and nums[idx] == nums[idx-1]: continue

            l = idx + 1
            r = len(nums) - 1
            while l<r:
                cum_sum = nums[idx] + nums[l] + nums[r]

                if cum_sum > 0:
                    r -= 1
                elif cum_sum < 0:
                    l += 1
                else:
                    output.append([nums[idx],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
        return output

"""
[1,2,0,-1,-1]
1) for loop: idx = 1 , l = 3, r = 4
2) while loop: cum_sum = 0
3) else : l = 4

"""
