class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmin, curmax = 1,1
        res = float("-inf")
        for i in nums:
            temp = curmax
            curmax = max(curmax*i, curmin*i, i)
            curmin = min(temp*i, curmin*i, i)
            res = max(res, curmax)
        return res