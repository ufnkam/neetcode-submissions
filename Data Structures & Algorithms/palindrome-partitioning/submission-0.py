class Solution:
    def partition(self, s: str) -> List[List[str]]:
        parts, curr_parts = [], []
        self._backtrack(s, 0, curr_parts, parts)
        return parts
        
    def _backtrack(
        self, 
        s: str, 
        start: int, 
        curr_parts: list[list[str]],
        parts: list[list[str]]
    ) -> None:
        if start == len(s):
            parts.append(curr_parts.copy()) 
            return
        for end in range(start + 1, len(s) + 1):
            part = s[start : end]
            if not self.is_palindrome(part): continue
            curr_parts.append(part)
            self._backtrack(s, end, curr_parts, parts)
            curr_parts.pop()
 
    def is_palindrome(self, s: str) -> bool:
        rev = s[::-1]
        return rev == s