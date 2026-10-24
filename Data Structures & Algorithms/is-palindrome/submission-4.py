class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = [c for c in s if c.isalnum()]
        
        s_rev = s.copy()
        l, r = 0, len(s_rev) - 1
        while l < r:
            s_rev[l], s_rev[r] = s_rev[r], s_rev[l]
            l += 1
            r -= 1

        return s_rev == s
