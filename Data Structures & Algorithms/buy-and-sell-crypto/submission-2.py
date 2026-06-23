class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        less = prices[0]
        maxi = 0
        for i in prices:
            maxi = max(maxi, i - less)
            less = min(less, i)
        return maxi