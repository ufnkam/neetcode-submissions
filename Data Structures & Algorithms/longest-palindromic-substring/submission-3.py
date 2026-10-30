class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0: return ""
        best = ""
        for i in range(n):
            odd = self._expand(i, i, s)
            even = self._expand(i, i + 1, s)
            best = max(odd, even, best, key=len)
        return best

    @staticmethod
    def _expand(l: int, r: int, s: str) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]
        
