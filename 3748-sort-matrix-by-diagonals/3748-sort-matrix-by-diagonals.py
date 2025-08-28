class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        for i in range(1, len(grid) - 1):
            temp = []
            x, y = 0, i
            while x < len(grid) and y < len(grid):
                temp.append(grid[x][y])
                x += 1
                y += 1
            temp.sort()
            x, y = 0, i
            while x < len(grid) and y < len(grid):
                grid[x][y] = temp[x]
                x += 1
                y += 1

        for i in range(len(grid) - 1):
            temp = []
            x, y = i, 0
            while x < len(grid) and y < len(grid):
                temp.append(grid[x][y])
                x += 1
                y += 1
            
            temp.sort()
            temp = temp[::-1]
            x, y = i, 0

            while x < len(grid) and y < len(grid):
                grid[x][y] = temp[y]
                x += 1
                y += 1

        return grid