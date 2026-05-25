class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for i,j in count.items():
            print(i)
            if j > 1:
                print(i)
                return True
            else:
                continue
        return False