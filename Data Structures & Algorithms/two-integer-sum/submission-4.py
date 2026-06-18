class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, elem in enumerate(nums):
            if target - elem in hashmap:
                return sorted([hashmap[target-elem], idx])
            else:
                hashmap[elem] = idx
            print(f"Dizionario: {hashmap}, indice {idx}")
    