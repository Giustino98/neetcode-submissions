import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.k = k
        while len(nums) > k:
            heapq.heappop(nums)
        self.nums = nums

    def add(self, val: int) -> int:
        heapq.heappush(self.nums,val)
        if len(self.nums) > self.k: heapq.heappop(self.nums)
        return self.nums[0]