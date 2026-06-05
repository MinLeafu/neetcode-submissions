class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            hs = set()
            for col in range(9):
                cell = board[row][col]
                if cell != ".":
                    if cell in hs:
                        return False
                    hs.add(cell)
        
        for col in range(9):
            hs = set()
            for row in range(9):
                cell = board[row][col]
                if cell != ".":
                    if cell in hs:
                        return False
                    hs.add(cell)
        
        for square in range(9):
            hs = set()
            for i in range(3):
                for j in range(3):
                    row = square // 3 * 3 + i
                    col = square % 3 * 3 + j
                    cell = board[row][col]
                    if cell != ".":
                        if cell in hs:
                            return False
                        hs.add(cell)

        return True