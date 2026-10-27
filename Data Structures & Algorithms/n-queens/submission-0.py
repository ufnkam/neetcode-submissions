arows = set()
acols = set()
adiags = set()
anti_adiags = set()

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0: return []
        # arows = set()
        # acols = set()
        # adiags = set()
        # anti_adiags = set()
        board = [["."] * n for _ in range(n)]
        boards = []
        # for i in range(n):
        self._backtrack(0, board, boards, n)
        return boards

    def _backtrack(
        self, 
        row: int, 
        board: list[list[str]],
        boards: list[list[str]],
        n: int
    ) -> None:
        if row == n:
            boards.append(self._construct_board(board))
            return
        
        for col in range(n):
            if not self._is_safe(row, col): continue
            board[row][col] = "Q"
            arows.add(row)
            acols.add(col)
            adiags.add(row - col)
            anti_adiags.add(row + col)
            self._backtrack(row + 1, board, boards, n)
            board[row][col] = "."
            arows.remove(row)
            acols.remove(col)
            adiags.remove(row - col)
            anti_adiags.remove(row + col)
    
    @staticmethod
    def _construct_board(board: list[list[str]]) -> list[str]:
        return ["".join(row) for row in board]

    @staticmethod
    def _is_safe(
        row: int, col: int
    ) -> bool:
        if row in arows: return False
        if col in acols: return False
        if (row - col) in adiags: return False
        if (row + col) in anti_adiags: return False
        return True