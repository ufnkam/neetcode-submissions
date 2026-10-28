from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: return -1
        rows, cols = len(grid), len(grid[0])
        queue = deque([])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 2: continue
                queue.append((i, j))
        max_dist = 2
        while queue:
            row, col = queue.popleft()
            for dr, dc in self._dirs():
                new_row, new_col = row + dr, col + dc
                if self._is_cell_valid(new_row, new_col, grid):
                    new_dist = grid[row][col] + 1
                    grid[new_row][new_col] = new_dist
                    max_dist = max(max_dist, new_dist)
                    queue.append((new_row, new_col))
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 1: continue
                return -1
        return max_dist - 2

    @staticmethod
    def _is_cell_valid(row: int, col: int, grid: [list[list[int]]]) -> bool:
        return (
            row >= 0
            and col >= 0
            and row < len(grid)
            and col < len(grid[0])
            and grid[row][col] == 1
        )

    @staticmethod
    def _dirs() -> list[tuple[int, int]]:
        return [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1)
        ]

        