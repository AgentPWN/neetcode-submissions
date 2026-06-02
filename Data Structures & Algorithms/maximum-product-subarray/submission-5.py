class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin, curMax = 1,1
        res = max(nums)
        for n in nums:
            tmp = curMax
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(tmp * n, curMin * n, n)
            res = max(curMax, res)
        return res