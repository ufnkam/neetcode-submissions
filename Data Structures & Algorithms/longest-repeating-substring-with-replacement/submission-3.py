class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s: return 0
        freq = {}
        longest = 0
        curr_freq = 0
        start = 0
        n = len(s)
        for end in range(n):
            freq[s[end]] = freq.get(s[end], 0) + 1
            curr_freq = max(freq.values())
            while end - start + 1 - curr_freq > k:
                freq[s[start]] -= 1
                curr_freq = max(freq.values())
                start += 1

            longest = max(longest, end - start + 1) 

        return longest