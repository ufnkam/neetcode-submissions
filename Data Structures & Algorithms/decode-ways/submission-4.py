class Solution:
    def numDecodings(self, s: str) -> int:
        if not s: return 0
        n = len(s)
        memo = [-1] * n
        self._backtrack(0, s, memo)
        return memo[0]
    
    def _backtrack(
        self,
        start: int,
        s: str,
        memo: list[int],
    ) -> int:
        if start == len(s):
            return 1
        if memo[start] != -1: return memo[start]
        ways = 0
        for _len in range(1, 3):
            if start + _len > len(s): break
            part = s[start:start + _len]
            if len(part) > 0 and part[0] == "0": break
            if int(part) > 26: break
            ways += self._backtrack(start + _len, s, memo)
            
        memo[start] = ways
        return ways