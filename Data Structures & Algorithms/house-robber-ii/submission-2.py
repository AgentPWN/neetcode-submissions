class Solution:
    def robhelp(self, num):
        rob1, rob2 = 0, 0
        for i in num:
            temp = max(rob2 + i, rob1)
            rob2 = rob1
            rob1 = temp
        return max(rob1, rob2)

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.robhelp(nums[:-1]), self.robhelp(nums[1:]))
    
        