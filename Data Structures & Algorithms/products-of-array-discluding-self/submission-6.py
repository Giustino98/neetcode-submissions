#prefix = [1,1,2,8]
#postfix = [48,24,6,1]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        
        cum_prod = 1
        for elem in nums:
            prefix.append(cum_prod)
            cum_prod = cum_prod * elem
        
        cum_prod = 1
        for elem in list(reversed(nums)):
            postfix.append(cum_prod)
            cum_prod = cum_prod * elem

        postfix.reverse()
        return [a*b for a,b in zip(prefix,postfix)]
