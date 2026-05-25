class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        productWith0 = 1
        num = set(nums)
        result = [0] * len(nums)
        count = Counter(nums)
        if count[0] > 1:
            return result
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            product = product * nums[i]
        print(product)
        if 0 in nums:
            for i in range(len(nums)):
                if nums[i] != 0:
                    continue
                else: 
                    result[i] = product
        else:
            for i in range(len(nums)):
                result[i] = int(product/nums[i])
        return result