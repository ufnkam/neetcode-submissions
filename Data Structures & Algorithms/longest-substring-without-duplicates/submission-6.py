class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        longest = 0
        n = len(s)
        store = {}
        start = 0

        for end in range(n):
            while store.get(s[end], 0) > 0:
                store[s[start]] = store[s[start]] - 1
                start += 1
                
            store[s[end]] = store.get(s[end], 0) + 1
            longest = max(longest, end - start + 1)
            
        return longest