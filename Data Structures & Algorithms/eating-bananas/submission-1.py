import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles: return 0
        l, r = 1, max(piles)
        best = float('inf')

        while l <= r:
            mid = l + (r - l) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
            if hours <= h:
                best = min(mid, best)
                r = mid - 1
            else:
                l = mid + 1
        return best


