class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        count = {}
        max_count = 0
        longest = 0
        left = 0

        for right in range(n):
            char = s[right]
            count[char] = count.get(char, 0) + 1
            max_count = max(max_count, count[char])

            if (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest
            


