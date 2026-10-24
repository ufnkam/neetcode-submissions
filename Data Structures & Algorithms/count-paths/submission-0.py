class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0

        memo = [[-1] * n for _ in range(m)]
        result = self._dp(0, 0, memo)
        return result

    def _dp(
        self,
        row: int,
        col: int,
        memo: int,
    ) -> int:
        if row == len(memo) - 1 and col == len(memo[0]) - 1:
            memo[row][col] = 1

        if memo[row][col] != -1:
            return memo[row][col]

        ways = 0
        for dr, dc in self._dirs():
            new_row = row + dr
            new_col = col + dc

            if self._is_cell_valid(new_row, new_col, memo):
                ways += self._dp(new_row, new_col, memo)

        memo[row][col] = ways
        return ways
        
    @staticmethod
    def _dirs() -> list[tuple[int, int]]:
        return [
            # (-1, 0),
            (0, 1),
            (1, 0),
            # (0, -1),
        ]

    @staticmethod
    def _is_cell_valid(row: int, col: int, grid: list[list[int]]) -> bool:
        return (
            row >= 0
            and col >= 0
            and row < len(grid)
            and col < len(grid[0])
        )
         