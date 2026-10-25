from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t): return ""
        freq_t = [0] * 128
        for c in t: freq_t[ord(c) - ord('a')] += 1
        t_non_zero = [i for i, f in enumerate(freq_t) if f > 0]
        freq_s = [0] * 128
        start = 0
        best = float('inf')
        best_start = 0
        for end in range(len(s)):
            freq_s[ord(s[end]) - ord('a')] += 1
            check = all([True if freq_t[i] <= freq_s[i] else False for i in t_non_zero])
            while check:
                if end - start + 1 < best:
                    best = end - start + 1
                    best_start = start
                freq_s[ord(s[start]) - ord('a')] -= 1
                start += 1
                check = all([True if freq_t[i] <= freq_s[i] else False for i in t_non_zero])

        return s[best_start:best_start + best] if best < float('inf') else ""
