from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid: return
        rows = len(grid)
        cols = len(grid[0])
        queue = deque([])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j))
        self._bfs(grid, queue)

    def _bfs(self, grid: list[list[int]], queue: deque) -> None:
        while queue:
            row, col = queue.popleft()
            for dr, dc in self._dirs():
                new_row = row + dr
                new_col = col + dc
                if self._is_cell_valid(new_row, new_col, grid):
                    grid[new_row][new_col] = grid[row][col] + 1
                    queue.append((new_row, new_col))

    @staticmethod
    def _dirs() -> list[tuple[int, int]]:
        return [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1)
        ]

    @staticmethod
    def _is_cell_valid(row: int, col: int, grid: list[list[int]]) -> bool:
        return (
            row >= 0
            and col >= 0
            and row < len(grid)
            and col < len(grid[0])
            and grid[row][col] == 2147483647
        )