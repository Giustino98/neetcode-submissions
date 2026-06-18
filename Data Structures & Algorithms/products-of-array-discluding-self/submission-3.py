class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []

        acc = 1
        prefix.append(acc)
        i = 1
        while i < len(nums):
            acc *= nums[i - 1]
            prefix.append(acc)
            i += 1
            
        acc = 1
        postfix.append(acc)
        i = len(nums) - 2
        while i > -1:
            acc *= nums[i + 1]
            postfix.append(acc)
            i -= 1
        postfix.reverse()

        print(prefix)
        print(postfix)

        return [a*b for a,b in zip(prefix,postfix)]