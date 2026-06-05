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
        
        hss = [set() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                cell = board[row][col]
                if cell != ".":
                    idx = row // 3 * 3 + col // 3
                    if cell in hss[idx]:
                        return False
                    hss[idx].add(cell)
        
        return True