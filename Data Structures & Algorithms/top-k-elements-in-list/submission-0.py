class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sup = {}
        count = 0
        values = []
        for i in nums:
            if i in sup:
                sup[i] += 1
            else:
                sup[i] = 1
        prices_sorted = dict(sorted(sup.items(), key=lambda item: item[1], reverse = True))
        a = len(prices_sorted)
        for i in prices_sorted:
            count = count + 1
            if count <=k:
                values.append(i) 
        return values