class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        # if len(s) == 1:
        #     return s[0]
            
        best = ""
        for i in range(len(s)):
            odd = self._expand(s, i, i)
            even = self._expand(s, i, i + 1)
            best = max(best, odd, even, key=len)
    
        return best

    def _expand(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1 : right]