from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        c1 = 0
        c2 = len(matrix)
        r1 = 0
        r2 = len(matrix[0]) - 1
        for c1 in range(c2):
            if target in matrix[c1]:
                return True
            else:
                continue
        return False