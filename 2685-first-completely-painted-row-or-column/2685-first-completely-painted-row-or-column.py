import numpy as np

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # Precompute the position of each number in the matrix
        position = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                position[mat[i][j]] = (i, j)

        # Initialize row and column counters
        m, n = len(mat), len(mat[0])
        row_count = [0] * m
        col_count = [0] * n

        # Process the array
        for i, num in enumerate(arr):
            r, c = position[num]
            row_count[r] += 1
            col_count[c] += 1

            # Check if a row or column is complete
            if row_count[r] == n or col_count[c] == m:
                return i