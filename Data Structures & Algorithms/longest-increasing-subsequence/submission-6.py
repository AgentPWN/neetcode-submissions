class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = len(nums) *[1]
        for i in range(len(nums)-2, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)
        return max(lis)