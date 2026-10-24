class Solution:
    def __init__(self) -> None:
        self.sol = ""

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.sol = ""
        if not board or not word:
            return False
        
        rows = len(board)
        cols = len(board[0])
        visited = [[False] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if board[row][col] != word[0]:
                    continue
                self._backtrack(
                    word,
                    board,
                    row,
                    col,
                    [board[row][col]],
                    visited
                )
                if self.sol:
                    return True

        return False
    
    def _backtrack(
        self,
        word: str,
        board: list[list[str]],
        row: int,
        col: int,
        curr: list[str],
        visited: list[list[bool]]
    ) -> None:
        if curr == list(word):
            self.sol = "".join(curr)
            return 

        visited[row][col] = True
        
        for dr, dc in self._directions():
            new_row = row + dr
            new_col = col + dc

            if (
                self._is_cell_valid(board, new_row, new_col)
                and not visited[new_row][new_col]
                and len(curr) < len(word)
                and board[new_row][new_col] == word[len(curr)]
            ):
                curr.append(board[new_row][new_col])
                self._backtrack(
                    word,
                    board,
                    new_row,
                    new_col,
                    curr,
                    visited
                )
                curr.pop()
                if self.sol:
                    visited[row][col] = False
                    break

        visited[row][col] = False

    @staticmethod
    def _is_cell_valid(grid: list[list[str]], row: int, col: int) -> bool:
        return (
            row >= 0
            and col >= 0
            and row < len(grid)
            and col < len(grid[0])
        )

    @staticmethod
    def _directions() -> list[tuple[int, int]]:
        return [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1)
        ]
        