class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2 or len(s2) < len(s1): return False
        s1_count = [0] * 26
        s2_count = [0] * 26
        for c in s1: s1_count[ord(c) - ord('a')] += 1
        start = 0 
        for end in range(len(s2)):
            s2_count[ord(s2[end]) - ord('a')] += 1
            if end - start + 1 > len(s1):
                s2_count[ord(s2[start]) - ord('a')] -= 1
                start += 1
            if s2_count == s1_count:
                return True
        
        return False
