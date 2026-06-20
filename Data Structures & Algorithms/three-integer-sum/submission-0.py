class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        output = []

        for idx,a in enumerate(sorted_nums[:-2]):
            if (idx>0 and a==sorted_nums[idx-1]): continue
            i = idx + 1
            j = len(sorted_nums) - 1
            while i < j:
                trip_sum = sorted_nums[i] + sorted_nums[j] + a
                if trip_sum > 0: j -= 1
                if trip_sum < 0: i += 1
                if trip_sum == 0:
                    output.append([sorted_nums[i], sorted_nums[j], a])
                    i += 1
                    while (sorted_nums[i] == sorted_nums[i-1] and i < j):
                        i+=1
        return output

