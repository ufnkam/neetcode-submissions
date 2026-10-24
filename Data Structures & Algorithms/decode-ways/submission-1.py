class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [-1] * len(s)
        return self._backtrack(
            s,
            0,
            memo
        )

    def _backtrack(
        self,
        s: str,
        start: int,
        memo: list[int],
    ) -> int:
        if start == len(s):
            return 1

        if memo[start] != -1:
            return memo[start]

        ways = 0
        for _len in range(1, 3):
            if start + _len > len(s):
                break

            part = s[start : start + _len]
            if part[0] == "0":
                break

            if int(part) > 26:
                break

            ways += self._backtrack(
                s,
                start + _len,
                memo,
            )

        memo[start] = ways
        return ways
