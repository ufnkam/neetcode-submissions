class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2: return 0
        rows, cols = len(text1), len(text2)
        memo = [[-1] * cols for _ in range(rows)]
        return self._dp(rows -1, cols - 1, text1, text2, memo)

    def _dp(
        self,
        row: int,
        col: int,
        text1: str,
        text2: str,
        memo: list[list[bool]],
    ) -> int:
        if row < 0 or col < 0: return 0
        if memo[row][col] != -1: return memo[row][col]
        if text1[row] == text2[col]:
            memo[row][col] = 1 + self._dp(row - 1, col - 1, text1, text2, memo)
            return memo[row][col]
        memo[row][col] = max(
            self._dp(row - 1, col, text1, text2, memo),
            self._dp(row, col - 1, text1, text2, memo)
        )
        return memo[row][col]
