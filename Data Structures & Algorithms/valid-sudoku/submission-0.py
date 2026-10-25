class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in board:
            seen=set()
            for c in r:
                if c in seen and c !=".":
                    return False
                elif c !=".":
                    seen.add(c)
        row = len(board)
        col = len(board[0])
        for i in range(col):
            seen = set()
            for j in range(row):
                if board[j][i] in seen and board[j][i] !=".":
                    return False
                elif board[j][i] !=".":
                    seen.add(board[j][i])
        
        for boxr in range(0,9,3):
            for colr in range(0,9,3):
                seen=set()
                for r in range(3):
                    for c in range(3):
                        cell = board[boxr+r][colr+c]
                        if cell!=".":
                            if cell in seen:
                                return False
                            seen.add(cell)
        return True



        