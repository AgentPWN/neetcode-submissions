class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums)):
            target = 0-nums[i]
            hash = {}
            for j in range(i+1,len(nums)):
                if nums[j] in hash.keys():
                    temp = [nums[i],nums[j],hash[nums[j]]]
                    temp.sort()
                    if temp not in result:
                        result.append(temp) 
                hash[target-nums[j]] = nums[j]
        return result