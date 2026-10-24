class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        curr_freq = 0
        freq = {}
        n = len(s)
        longest = 0

        start = 0
        for end in range(n):
            freq[s[end]] = freq.get(s[end], 0) + 1
            curr_freq = max(freq.values())
            while (end - start + 1) - curr_freq > k:
                freq[s[start]] -= 1
                start += 1
                curr_freq = max(freq.values())

            longest = max(longest, end - start + 1)
        return longest
