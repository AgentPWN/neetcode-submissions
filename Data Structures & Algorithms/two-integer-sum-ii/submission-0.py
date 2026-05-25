class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(numbers)):
            if numbers[i] in hash.keys():
                return [hash[numbers[i]]+1,i+1]
            hash[target - numbers[i]] = i