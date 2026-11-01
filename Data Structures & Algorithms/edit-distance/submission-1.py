class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows, cols = len(word1), len(word2)
        memo = [[-1] * cols for _ in range(rows)]
        return self._dp(rows - 1, cols - 1, word1, word2, memo)

    def _dp(
        self,
        row: int, 
        col: int,
        word1: str,
        word2: str,
        memo: list[list[int]]
    ) -> int:
        if row < 0: return col + 1
        if col < 0: return row + 1
        if memo[row][col] != -1: return memo[row][col]
        if word1[row] == word2[col]:
            memo[row][col] = self._dp(row - 1, col - 1, word1, word2, memo)
            return memo[row][col]
        memo[row][col] = 1 + min(
            self._dp(row - 1, col, word1, word2, memo), # delete
            self._dp(row, col - 1, word1, word2, memo), # insert
            self._dp(row - 1, col - 1, word1, word2, memo), # change
        )
        return memo[row][col]
