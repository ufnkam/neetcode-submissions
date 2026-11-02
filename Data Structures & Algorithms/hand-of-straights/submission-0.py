from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0: return False
        counter = Counter(hand)
        counted = [k for k in counter]
        counted = sorted(counted)
        for c in counted:
            count = counter[c]
            if count == 0: continue
            for val in range(c, c + groupSize):
                if counter[val] < count: return False
                counter[val] -= count
        return True

