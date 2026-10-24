class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        s1 = sorted(s1)
        left = 0
        n = len(s2)

        for right in range(m, n + 1, 1):
            sub = sorted(s2[left:right])
            if sub == s1:
                return True
            
            left += 1

        return False
        

