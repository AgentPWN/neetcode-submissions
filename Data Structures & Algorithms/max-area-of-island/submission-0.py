class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        area = 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        def bfs(r, c):
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            q = collections.deque()
            q.append([r,c])
            area = 1
            visit.add((r,c))
            while q:
                row, col = q.popleft()
                for dr,dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and c in range(cols) 
                    and (r,c) not in visit and grid[r][c] == 1):
                        area += 1
                        q.append([r,c])
                        visit.add((r,c))
            return area
            area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = bfs(r,c)
                    maxArea = max(maxArea, area)
        return maxArea