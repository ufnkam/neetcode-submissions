class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 0: return 0
        counter = 0
        for i in range(n):
            counter += self._expand(i, i, s)
            counter += self._expand(i, i + 1, s)
        return counter

    @staticmethod
    def _expand(l: int, r: int, s: str) -> int:
        counter = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            counter += 1
            l -= 1
            r += 1
        return counter