class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1
        res = max(nums)
        while l <= r:
            if nums[l] <= nums[r]:
                return min(res, nums[l])
            m = (l+r)//2
            res = min(res, nums[m])
            print(res)
            if nums[m] >= nums[r]:
                l = m + 1
            else:
                r = m - 1
        return res 