class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        mini = r
        mid = 0
        while l <= r:
            mid = (l+r)//2
            hours = 0
            print(mid)
            for i in piles:
                hours += math.ceil(i/mid)
            if hours <= h:
                mini = min(mini, mid)
                r = mid - 1
            else:
                l = mid + 1

        return mini