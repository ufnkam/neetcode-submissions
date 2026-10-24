class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        curr_freq = 0
        start = 0
        longest = 0
        n = len(s)
        for end in range(n):
            c = s[end]
            freq[c] = freq.get(c, 0) + 1
            curr_freq = max(freq.values())
            while (end - start + 1) - curr_freq > k:
                freq[s[start]] -= 1
                start += 1
                curr_freq = max(freq.values())

            longest = max(longest, end - start + 1)

        return longest
