class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []

        acc = 1
        for i in range (len(nums)):
            if i == 0: 
                prefix.append(1)
                continue
            acc = nums[i-1] * acc
            prefix.append(acc)

        acc = 1
        for i in reversed(range(len(nums))):
            if i == len(nums) - 1: 
                postfix.append(1)
                continue
            acc = nums[i + 1] * acc
            postfix.append(acc)
        
        postfix = reversed(postfix)

        return [a*b for a,b in zip(prefix,postfix)]