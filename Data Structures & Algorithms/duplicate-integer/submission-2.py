from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for i in counter.values():
            if i > 1:
                return True

        return False
