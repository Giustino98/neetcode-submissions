class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        postfix = [1]

        temp = nums[0]
        for elem in nums[1:]:
            prefix.append(temp)
            temp *= elem
        
        temp = nums[-1]
        for elem in list(reversed(nums))[1:]:
            postfix.append(temp)
            temp *= elem
        postfix.reverse()

        return [a*b for a,b in zip(prefix,postfix)]