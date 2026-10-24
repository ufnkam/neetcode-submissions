class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        m = len(text1)
        n = len(text2)
        memo = [[-1] * n for _ in range(m)]
        return self._dp(m - 1, n - 1, text1, text2, memo)


    def _dp(
        self,
        row: int,
        col: int,
        s1: str,
        s2: str,
        memo: list[list[int]]
    ) -> int:
        if row < 0 or col < 0:
            return 0

        if memo[row][col] != -1:
            return memo[row][col]

        if s1[row] == s2[col]:
            memo[row][col] = 1 + self._dp(row - 1, col - 1, s1, s2, memo)
            return memo[row][col]

        memo[row][col] = max(
            self._dp(row - 1, col, s1, s2, memo),
            self._dp(row, col - 1, s1, s2, memo)
        )
        return memo[row][col]

        