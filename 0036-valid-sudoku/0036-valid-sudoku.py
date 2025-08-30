class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            rows = []
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] not in rows:
                        rows.append(board[i][j])
                    else:
                        return False
                 
        for j in range(9):
            cols = []
            for i in range(9):
                if board[i][j] != ".":
                    if board[i][j] not in cols:
                        cols.append(board[i][j])
                    else:
                        return False
        
        boxes = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":  # skip empty cells
                    continue

                boxIndex = (r // 3) * 3 + (c // 3)

                # Check for duplicate inside this box
                if val in boxes[boxIndex]:
                    return False  # duplicate found → invalid

                boxes[boxIndex].add(val)

        return True