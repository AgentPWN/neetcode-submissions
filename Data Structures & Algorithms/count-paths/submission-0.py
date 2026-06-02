class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * m
        for i in range(n-1):
            newrow = [1] * m
            for j in range(m-2, -1, -1):
                newrow[j] = newrow[j+1] + row[j]

            row = newrow
        return row[0]