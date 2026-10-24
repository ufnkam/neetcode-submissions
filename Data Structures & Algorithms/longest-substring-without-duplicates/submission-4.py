class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 1
        n = len(s)
        left = 0

        if not s:
            return 0

        current_set = {s[left]: left}
        for right in range(1, n):
            char = s[right]
            if char in current_set and current_set[char] >= left:
                left = current_set[char] + 1

            current_set[char] = right
            longest = max(longest, right - left + 1)

        return longest