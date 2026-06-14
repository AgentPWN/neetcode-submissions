class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visit = set()
        q = deque()
        rows, cols = len(grid), len(grid[0])
        def adddata(r,c):
            if r < 0 or r == rows or c < 0 or c == cols or (r,c) in visit or grid[r][c] == -1:
                return
            q.append([r,c])
            visit.add((r,c))
    
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append([i,j])
                    visit.add((i,j))
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                adddata(r+1,c)
                adddata(r-1,c)
                adddata(r,c+1)
                adddata(r,c-1)
                grid[r][c] = dist
            dist += 1
