class Solution:
    from collections import deque

    def numIslands(self, grid: List[List[str]]) -> int:
        out = 0
        n_rows, n_cols = len(grid), len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == "1":
                    out += 1

                    # traverse subgraph aka island
                    stack = deque([(r, c)]) # for O(1) pop first
                    while stack:
                        r0, c0 = stack.pop()
                        if 0 <= r0 < n_rows and 0 <= c0 < n_cols and grid[r0][c0] == "1":
                            grid[r0][c0] = "0"
                            for rd, cd in dirs:
                                stack.append((r0 + rd, c0 + cd))
            
        return out
