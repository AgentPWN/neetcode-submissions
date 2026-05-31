class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 0:
            return [[]]
        perm = self.permute(nums[1:])
        for i in perm:
            for j in range(len(i)+1):
                i_copy = i.copy()
                i_copy.insert(j,nums[0])
                res.append(i_copy)
        return res