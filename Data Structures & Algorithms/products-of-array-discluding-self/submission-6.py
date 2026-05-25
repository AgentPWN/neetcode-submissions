class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        n = len(nums)
        result = [0] * n
        count = Counter(nums)
        if count[0] > 1:
            return result
        for i in range(n):
            if nums[i] == 0:
                continue
            product = product * nums[i]
        if 0 in nums:
            for i in range(n):
                if nums[i] != 0:
                    continue
                else: 
                    result[i] = product
        else:
            for i in range(n):
                result[i] = int(product/nums[i])
        return result