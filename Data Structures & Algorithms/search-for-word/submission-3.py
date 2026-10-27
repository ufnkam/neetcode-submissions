class Solution:
    def __init__(self) -> None:
        self.sol = ""

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word: return False
        rows = len(board)
        cols = len(board[0])
        visited = [[False] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if not board[i][j] == word[0]:
                    continue
                self._backtrack(board, i, j, visited, [board[i][j]], word)
                if self.sol: return True
        return False

    def _backtrack(
        self,
        board: list[list[str]],
        row: int,
        col: int,
        visited: list[list[bool]],
        comb: list[str],
        word: str,
    ) -> None:
        if len(comb) == len(word):
            self.sol = "".join(comb)
            return
        visited[row][col] = True

        for dr, dc in self._dirs():
            new_row = row + dr
            new_col = col + dc
            if (
                self.is_cell_valid(new_row, new_col, board)
                and not visited[new_row][new_col]
                and board[new_row][new_col] == word[len(comb)] 
            ): 
                comb.append(board[new_row][new_col])
                self._backtrack(board, new_row, new_col, visited, comb, word)
                comb.pop()
                
                if self.sol:
                    visited[row][col] = False
                    return 

        visited[row][col] = False

    @staticmethod
    def _dirs() -> list[tuple[int, int]]:
        return [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1)
        ]

    @staticmethod
    def is_cell_valid(row: int, col: int, grid: list[list[str]]) -> bool:
        return (
            row >= 0
            and col >= 0
            and row < len(grid)
            and col < len(grid[0])
        )



        