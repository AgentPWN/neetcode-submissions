class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # maxheap = [-n for n in nums]
        i = len(nums) - k
        # heapq.heapify(maxheap)
        heapq.heapify(nums)
        while i >= 1:
            i -= 1
            heapq.heappop(nums)
        return nums[0]