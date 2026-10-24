class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = {}

        start = 0
        longest = 0
        for end in range(len(s)):
            c = s[end]
            store[c] = store.get(c, 0) + 1
            while store[c] > 1:
                store[s[start]] -= 1
                start += 1

            longest = max(longest, end - start + 1)
            
        return longest