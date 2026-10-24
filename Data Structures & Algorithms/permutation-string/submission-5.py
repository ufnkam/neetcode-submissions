class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        need = Counter(s1)
        window = Counter(s2[:n1])
        if window == need:
            return True

        for i in range(n1, n2):
            window[s2[i]] += 1
            window[s2[i - n1]] -= 1
            if window == need:
                return True

        return False

        

