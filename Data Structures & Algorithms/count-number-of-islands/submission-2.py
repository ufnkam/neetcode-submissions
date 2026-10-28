class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid : return 0
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '0' or visited[i][j]: continue
                island = []
                self._dfs(i, j, grid, visited, island)
                if island: islands += 1
        return islands

    def _dfs(
        self, 
        row: int, 
        col: int, 
        grid: list[list[str]], 
        visited: list[list[bool]],
        island: list[tuple[int ,int]],
    ) -> None:
        visited[row][col] = True
        island.append((row, col))
        for dr, dc in self._dirs():
            new_row = row + dr
            new_col = col + dc
            if (
                self._is_cell_valid(new_row, new_col, grid)
                and not visited[new_row][new_col]
            ):
                self._dfs(new_row, new_col, grid, visited, island)


    @staticmethod
    def _is_cell_valid(row: int, col: int, grid: [list[list[str]]]) -> bool:
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