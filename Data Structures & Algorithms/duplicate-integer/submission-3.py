class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for idx,elem in enumerate(nums):
            print(f"Elem 1 to compare: {elem} \n")
            for elem_to_compare in nums[idx + 1 :]:
                print(f"Elem 1 compared to: {elem_to_compare} \n")
                if elem == elem_to_compare: return True
        return False
