class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = defaultdict(int)
        n = len(nums)
        top = [[] for _ in range(n)]
        topK = []
        count = 0
        for i in range(n):
            hash[nums[i]]+= 1        
        for i,j in hash.items():
            top[j-1].append(i)
        for i in top[::-1]:
            for j in i:
                topK.append(j)
            if len(topK) == k:
                return topK