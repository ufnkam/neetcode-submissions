from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_1 = Counter(s)
        counter_2 = Counter(t)

        return counter_1 == counter_2