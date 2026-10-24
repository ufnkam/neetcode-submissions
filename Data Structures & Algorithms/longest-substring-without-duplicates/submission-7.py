class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        n = len(s)
        freq = {}
        longest = 0
        start = 0
        for end in range(n):
            c = s[end]
            while freq.get(c, 0) > 0:
                freq[s[start]] -= 1
                start += 1
            freq[c] = freq.get(c, 0) + 1
            longest = max(longest, end - start + 1)

        return longest