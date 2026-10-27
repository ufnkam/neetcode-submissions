class Solution:
    def partition(self, s: str) -> List[List[str]]:
        parts, curr_parts = [], []
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                is_pal[i][j] = s[i] == s[j] and (j - i < 2 or is_pal[i + 1][j - 1])
        self._backtrack(s, 0, curr_parts, parts, is_pal)
        return parts
        
    def _backtrack(
        self, 
        s: str, 
        start: int, 
        curr_parts: list[list[str]],
        parts: list[list[str]],
        is_pal: list[list[bool]],
    ) -> None:
        if start == len(s):
            parts.append(curr_parts.copy()) 
            return
        for end in range(start + 1, len(s) + 1):
            part = s[start : end]
            if not is_pal[start][end - 1]: continue
            curr_parts.append(part)
            self._backtrack(s, end, curr_parts, parts, is_pal)
            curr_parts.pop()
 