from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if -(nums[i] + nums[j]) in nums[j+1:]:
                    triplet = sorted([nums[i], nums[j], -(nums[i] + nums[j])])
                    if triplet not in sol:
                        sol.append(triplet)
                        print(sol)
        return sol
