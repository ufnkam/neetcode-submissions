class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2: return False
        count1 = [0] * 26
        for c in s1:
            count1[ord(c) - ord('a')] += 1
        count2 = [0] * 26
        start = 0
        for end in range(len(s2)):
            count2[ord(s2[end]) - ord('a')] += 1

            if end - start + 1 > len(s1):
                count2[ord(s2[start]) - ord('a')] -= 1
                start += 1

            if count1 == count2:
                return True

        return False