from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board: return
        rows, cols = len(board), len(board[0])

        visited = [[False] * cols for _ in range(rows)]
        queue = deque([])
        for i in range(rows):
            for j in range(cols):
                if not board[i][j] == "O": continue
                if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                    queue.append((i, j))
        connected: set[tuple[int, int]] = set()
        while queue:
            row, col = queue.popleft()
            visited[row][col] = True
            connected.add((row, col))
            for dr, dc in self._dirs():
                new_row, new_col = row + dr, col + dc
                if (
                    self._is_cell_valid(new_row, new_col, board)
                    and not visited[new_row][new_col]
                ):
                    queue.append((new_row, new_col))
        for i in range(rows):
            for j in range(cols):
                if (i, j) in connected or board[i][j] == "X": 
                    continue
                board[i][j] = "X"

    @staticmethod
    def _dirs() -> list[tuple[int, int]]:
        return [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1)
        ]

    @staticmethod
    def _is_cell_valid(row: int, col: int, grid: list[list[str]]) -> bool:
        return (
            row >= 0
            and col >= 0
            and row < len(grid)
            and col < len(grid[0])
            and grid[row][col] == "O"
        )