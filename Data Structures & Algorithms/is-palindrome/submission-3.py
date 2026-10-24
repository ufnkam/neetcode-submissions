class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        x = [c for c in s if c.isalnum()]

        rev = x.copy()
        left, right = 0, len(rev) - 1

        while left < right:
            rev[left], rev[right] = rev[right], rev[left]
            left += 1
            right -= 1

        return x == rev
        
