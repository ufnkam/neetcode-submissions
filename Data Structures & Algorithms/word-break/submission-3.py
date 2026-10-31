class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)
        memo = [-1] * len(s)
        return self._dp(0, wordset, s, memo)

    def _dp(
        self, 
        start: int,
        wordset: set[str],
        s: str,
        memo: list[int],
    ) -> bool:
        if start == len(s): return True
        if start > len(s): return False
        if memo[start] != -1: return memo[start]
        for end in range(start + 1, len(s) + 1):
            part = s[start : end]
            if part not in wordset: continue
            if self._dp(end, wordset, s, memo):
                memo[start] = True
                return True
        memo[start] = False
        return False

