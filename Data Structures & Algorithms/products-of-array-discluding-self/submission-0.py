class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        a = []
        count = 0
        for i in nums:
            if i != 0:
                product = product*i
            else:
                count += 1
        for i in nums:
            if count == 0:
                a.append(int(product/i))
            elif count == 1:
                if i == 0:
                    a.append(product)
                else:
                    a.append(0)
            else:
                a.append(0)
        return a