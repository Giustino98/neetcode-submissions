class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l<=r:
            temp_sum = numbers[l] + numbers[r]
            if temp_sum < target:
                l +=1
            elif temp_sum > target:
                r -=1
            else: return [l+1,r+1]