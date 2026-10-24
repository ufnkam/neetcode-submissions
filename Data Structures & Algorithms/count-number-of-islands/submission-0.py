class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        islands = []

        for row in range(rows):
            for col in range(cols):
                if visited[row][col] or grid[row][col] == "0":
                    continue
                
                island = []
                self._dfs(
                    grid,
                    row,
                    col,
                    island,
                    visited,
                )
                islands.append(island)

        return len(islands)
        
    def _dfs(
        self,
        grid: list[list[str]],
        row: int,
        col: int,
        island: list[tuple[int, int]],
        visited: list[list[bool]],
    ) -> None:
        visited[row][col] = True

        for dr, dc in self._dirs():
            new_row = row + dr
            new_col = col + dc

            if (
                self._is_cell_valid(
                    grid, new_row, new_col
                )
                and not visited[new_row][new_col]
            ):
                island.append((new_row, new_col))
                self._dfs(
                    grid,
                    new_row,
                    new_col,
                    island,
                    visited
                )
        

    @staticmethod
    def _is_cell_valid(grid: list[list[str]], row: int, col: int) -> bool:
        return (
            row >= 0
            and col >= 0
            and row < len(grid)
            and col < len(grid[0])
            and grid[row][col] == "1"
        )

    @staticmethod
    def _dirs() -> list[tuple[int, int]]:
        return [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1)
        ]