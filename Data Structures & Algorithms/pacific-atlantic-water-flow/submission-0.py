from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return []
        pacific = self._bfs(0, 0, heights)
        atlantic = self._bfs(len(heights) - 1, len(heights[0]) - 1, heights)
        result = set()
        for vec in pacific:
            if vec in atlantic: result.add(vec)
        return list(list(vec) for vec in result)

    def _bfs(self, row: int, col: int, grid: list[list[int]]) -> set[tuple[int, int]]:
        queue = deque([])
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        ocean = set()
        for j in range(len(grid[0])): queue.append((row, j))
        for i in range(len(grid)): queue.append((i, col))
        while queue:
            _row, _col = queue.popleft()
            visited[_row][_col] = True
            ocean.add((_row, _col))
            for dr, dc in self._dirs():
                new_row, new_col = _row + dr, _col + dc
                if (
                    self._is_cell_valid(new_row, new_col, grid)
                    and not visited[new_row][new_col]
                    and grid[new_row][new_col] >= grid[_row][_col]
                ):
                    queue.append((new_row, new_col))
        return ocean
    
    @staticmethod
    def _is_cell_valid(row: int, col: int, grid: [list[list[int]]]) -> None:
        return (
            row >= 0 
            and col >= 0
            and row < len(grid)
            and col < len(grid[0])
        )
    
    @staticmethod
    def _dirs() -> list[tuple[int, int]]:
        return [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1)
        ]