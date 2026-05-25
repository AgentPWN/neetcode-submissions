class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                height = heights[i] if heights[i]<heights[j] else heights[j]
                temp = abs((i-j)*(height))
                if temp > area:
                    area = temp
        return area