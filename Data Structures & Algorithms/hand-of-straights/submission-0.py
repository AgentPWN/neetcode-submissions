class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = {}
        if len(hand) % groupSize != 0:
            return False
        for i in hand:
            count[i] = count.get(i, 0) + 1
        heap = list(count.keys())
        heapq.heapify(heap)
        while heap:
            first = heap[0]
            for i in range(first, first + groupSize):
                if i not in count:
                    print(i)
                    print("wtf")
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != heap[0]:
                        return False
                    heapq.heappop(heap)
            
        return True