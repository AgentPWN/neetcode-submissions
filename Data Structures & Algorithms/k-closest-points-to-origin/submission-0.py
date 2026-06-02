class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for i in points:
            minheap.append([i[0]**2 + i[1]**2, i[0], i[1]])
        heapq.heapify(minheap)
        res = []
        while k:
            dist, x, y = heapq.heappop(minheap)
            res.append([x,y])
            k -= 1
        return res