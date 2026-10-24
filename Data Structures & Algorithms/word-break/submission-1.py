class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dict = set(wordDict)
        memo = [-1] * len(s)
        return self._dp(s, 0, word_dict, memo)

    def _dp(
        self,
        s: str,
        start: int,
        word_dict: set[str],
        memo: list[int],
    ) -> bool:
        if len(s) == start:
            return True

        if start > len(s):
            return False

        if memo[start] != -1:
            return memo[start]

        for end in range(start + 1, len(s) + 1):
            part = s[start : end]

            if part not in word_dict:
                continue

            if self._dp(
                s,
                end,
                word_dict,
                memo
            ):
                memo[start] = True
                return True

        memo[start] = False
        return False