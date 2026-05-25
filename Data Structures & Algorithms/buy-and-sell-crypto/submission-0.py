class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i,r = 0,1
        profit = 0
        while r < len(prices):
            if prices[i] < prices[r]:
                profit = max(profit,prices[r]-prices[i])
            else: 
                i = r
            r += 1
        return profit